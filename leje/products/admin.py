from django.contrib import admin
from .models import UserProfile, Direction, RankingUser, Category, Product, Card, Rent



class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','cellphone','bday') 


# class UserDirectionAdmin(admin.ModelAdmin):
#     list_display = ('street','int_number','ext_number','neighborhood','country','state')


# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Direction)
admin.site.register(RankingUser)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Card)
admin.site.register(Rent)