from django.shortcuts import render, HttpResponse, redirect
from django.contrib.messages import error
import bcrypt
from models import *

def index(request):
    return render(request,'test_app/index.html')

def dashboard(request):
    user_items = Item.objects.filter(created_by_id = request.session["user_id"])
    other_users_items = Item.objects.exclude(created_by_id = request.session["user_id"]).exclude(added_by_users = request.session["user_id"])
    user = User.objects.get(id=request.session["user_id"])
    user_name = User.objects.get(id=request.session["user_id"]).first_name
    user_added_items = user.added_items.all()
    context = {
        "user_items" : user_items,
        "other_users_items": other_users_items,
        "user_added_items": user_added_items,
        "user_name": user_name
    }

    return render(request,'test_app/display.html', context)

def new(request):
    return render(request,'test_app/add.html')

def show(request,id):
    item = Item.objects.get(id=id)
    users_name = Item.objects.get(id=id).added_by_users.all()
    context = {
        "item": item,
        "users_name": users_name
    }
    return render(request,'test_app/show.html', context)


def authentification(request):
    pwd = User.objects.filter(email=request.POST["email"]).values("password")
    if len(pwd) == 0:
        return redirect("/main")
    # to check if the password are equal
    hash1 = pwd[0]["password"]
    pwd2=request.POST["pwd"]
    if bcrypt.checkpw(pwd2.encode(), hash1.encode()):
        request.session["user_id"] = User.objects.get(email=request.POST["email"]).id
        return redirect("/dashboard")
    else:
        return redirect("/main")
def logout(request):
    request.session["user_id"] = 0
    return redirect("/main")

def create(request):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/main')
    pwd_hash = bcrypt.hashpw(request.POST["pwd"].encode(), bcrypt.gensalt())
    User.objects.create(first_name=request.POST["f_name"],
    last_name=request.POST["l_name"], email= request.POST["email"], password= pwd_hash, date_hired= request.POST["date"])
    request.session["user_id"] = User.objects.get(email=request.POST["email"]).id

    return redirect("/dashboard")


def create_item(request):
    if request.method == "POST":
        item_name = request.POST["item"]
        created_by = User.objects.get(id = request.session["user_id"])
        if len(item_name) < 3:
            return redirect("/wish_items/create")
        else:
            Item.objects.create(name=item_name, created_by= created_by)
            return redirect("/dashboard")

def delete_item(request, id):
    Item.objects.get(id=id).delete()
    return redirect("/dashboard")

def add_wish_item(request, id):
    this_item = Item.objects.get(id=id)
    this_user = User.objects.get(id=request.session["user_id"])
    this_item.added_by_users.add(this_user)
    return redirect("/dashboard")

def remove_wish_item(request, id):
    this_item = Item.objects.get(id=id)
    this_user = User.objects.get(id=request.session["user_id"])
    this_item.added_by_users.remove(this_user)
    return redirect("/dashboard")
