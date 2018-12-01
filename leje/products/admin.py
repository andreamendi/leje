from django.contrib import admin
from .models import UserProfile, Direction



class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','cellphone') 

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)


# class UserDirectionAdmin(admin.ModelAdmin):
#     list_display = ('street','int_number','ext_number','neighborhood','country','state')
# admin.site.register(UserProfile, UserDirectionAdmin)