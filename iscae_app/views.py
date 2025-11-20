from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .forms import ItemForm   # important
from iscae_app.models import CustomUser, Item


def say_hello(request):
    return HttpResponse("Say Hello")




def say_hello_json(request):
    return JsonResponse({"Say Hello":"Say Hello"})




def html_page(request):
    users = CustomUser.objects.all()
    return render(request,'index.html',context={"nom":"mohamed","users":users})





def list_item(request):
    items = Item.objects.all()
    return render(request, 'items.html', context={"items":items})



def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_item')
    else:
        form = ItemForm()
    return render(request, 'index.html', {'form': form})

from django.shortcuts import get_object_or_404

def item_update(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('list_item')
    else:
        form = ItemForm(instance=item)

    return render(request, 'item_update.html', {'form': form, 'item': item})

def item_delete(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('list_item')

    return render(request, 'item_delete_confirm.html', {'item': item})


