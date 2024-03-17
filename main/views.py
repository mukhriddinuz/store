from django.shortcuts import render
from .models import *

def index_view(request):
    contex = {
        'banner':Banner.objects.all().order_by('-id')[:2],
        'shop_collection':Shop_colloection.objects.all().order_by('-id')[:9],
        'products':Products.objects.all().order_by('-id')[:8],
        'new_products':New_Products.objects.all().order_by('-id')[:6],
        'treding_ats':Treding_ats.objects.all().order_by('-id')[:2],
        'brand':Brand.objects.all().order_by('-id')[:7],
        'contact':Contact.objects.last(),




    }
    return render(request, "index.html",contex)
