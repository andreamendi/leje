from django.contrib import admin
from .models import UserProfile, Direction



class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','cellphone','bday') 


# class UserDirectionAdmin(admin.ModelAdmin):
#     list_display = ('street','int_number','ext_number','neighborhood','country','state')


# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)


