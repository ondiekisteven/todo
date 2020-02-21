from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from .models import Item
from django.contrib import messages
from django.contrib.auth.models import User


def index(request, username):
    if not request.user.is_authenticated:
        return render(request, 'todo/bad_request.html')
    items = Item.objects.filter(created_by__username=username).all()
    context = {
        'all_items': items
    }
    return render(request, 'list/index.html', context=context)


def add_item(request, username):
    item_to_add = request.POST["content"]
    user = User.objects.get(username=username)
    new_item = Item(item_content=item_to_add, created_by=user)
    new_item.save()
    messages.success(request, f'New TODO item added. Title: {item_to_add}')
    return HttpResponseRedirect("/")


def delete_item(request, item_id, username):
    item_to_delete = Item.objects.get(id=item_id, created_by__username=username)
    item_to_delete.delete()
    messages.warning(request, f'\'{item_to_delete}\' had been deleted successfully')
    return HttpResponseRedirect("/")


def list_items(request):
    all_items = Item.objects.all()
    data = {'result': list(all_items.values('item_content', 'date_created'))}
    return JsonResponse(data)


def get_item(request, item_id):

    item = Item.objects.get(id=item_id)
    if item:
        data = {
            'id': item.id,
            'content': item.item_content,
            'created': item.date_created
        }
    else:
        data = {
            'error': 'Id does not exist'
        }
    return JsonResponse(data)