from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from pdbapp.models import Item, Category


def index(request):
    template = loader.get_template('index.html')
    context = {
        'categories' : Category.objects.all()
    }
    return HttpResponse(template.render(context,request))

def item(request,item_id):
    template = loader.get_template('item.html')
    try:
        itm = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        itm = None
    context = {
        'item' : itm
    }
    return  HttpResponse(template.render(context,request))