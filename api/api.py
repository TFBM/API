from tastypie.resources import ModelResource, Resource
from django.conf.urls import url
from tastypie.authorization import Authorization
#Changing for bitAuth
#from tastypie.authentication import ApiKeyAuthentication
from tastypie import fields
from tastypie.constants import ALL
from django.contrib.auth.models import User
from tastypie.exceptions import Unauthorized


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username']