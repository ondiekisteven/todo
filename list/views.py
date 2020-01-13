from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Item


def index(request):
    items = Item.objects.all().order_by('-pk')
    context = {
        'all_items':items
    }
    return render(request, 'index.html', context=context)


def add_item(request):
    item_to_add = request.POST["content"]
    new_item = Item(item_content=item_to_add)
    new_item.save()
    return HttpResponseRedirect("/")


def delete_item(request, item_id):
    item_to_delete = Item.objects.get(id=item_id)
    item_to_delete.delete()
    return HttpResponseRedirect("/")