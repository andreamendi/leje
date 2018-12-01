from django.shortcuts import render

# Create your views here.

from .models import Category

def index(request):
    category_list = Category.objects.all()
    context = {
        'category_list' : category_list
    }
    return render(request, 'products/index.html', context)
