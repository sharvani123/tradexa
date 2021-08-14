
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, UserManager
)
from django.db.models import fields
from django.db.models.base import Model
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email=None, first_name=None, last_name=None, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("user must have an email address")
        if not password:
            raise ValueError('user must have a passowrd')
        user_obj =self.model (
            email = self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user_obj.set_password(password)
        user_obj.staff=is_staff
        user_obj.admin=is_admin
        user_obj.active=is_active
        user_obj.save(using=self._db)
        return user_obj
    
    def create_staffuser(self, username, email=None,first_name=None, last_name=None, password=None):
        user =self.create_user(
            email, 
            first_name,
            last_name,
            username,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, username, email=None, first_name=None, last_name=None, password=None):
        user =self.create_user(
            email, 
            first_name,
            last_name,
            username,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user

class User(AbstractBaseUser):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=255,unique=True)
    username=models.CharField(max_length=100,unique=True)

    active =models.BooleanField(default=True)
    staff =models.BooleanField(default=False)
    admin =models.BooleanField(default=False)
    timestmap=models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD='username'

    REQUIRED_FIELDS=[]

    objects= UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_lable):
        return True
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.active
    

class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField(null=True, blank=True)
    created_at=models.DateTimeField(null=True, blank=True)
    updated_at=models.DateTimeField(null=True, blank=True)