from __future__ import unicode_literals
from django.db import models
import re
from myemail import Email
from name import Name
from password import Password
import traceback

class UserManager(models.Manager):
    
    def validate(self, post_data):
        errors = {}
        valid_first_name = "django"
        valid_last_name  = "django"
        try:
            Name(post_data["f_name"], valid_last_name)
        except Exception as e:
            errors["f_name"] = str(e)
        try:
            Name(valid_first_name, post_data["l_name"])
        except Exception as e:
            errors["l_name"] = str(e)
        try:
            Password(post_data["pwd"], post_data["confi_pwd"])
        except Exception as e:
            errors["pwd"] = str(e)
            traceback.print_exc()

        # check email field for valid email
        try:
            Email(post_data['email'])
        except Exception as e:
            errors['email'] = str(e)

        # if email is valid check db for existing email
        if "email" not in errors:
            if len(self.filter(email=post_data['email'])) >= 1:
                errors['email'] = "email already in use"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    date_hired = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __str__(self):
        return self.email

class Item(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    #user can create many Items
    created_by = models.ForeignKey(User, related_name = "created_items")
    #there is a many to many relationship between items and users
    # users can add many items and items can be added by many users
    added_by_users = models.ManyToManyField(User, related_name="added_items")
