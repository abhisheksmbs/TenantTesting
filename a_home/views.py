from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item

def home_view(request):
    items = Item.objects.all()  # Assuming you want to display items from the Item model
    context = {
        'items': items
    }
    return render(request, 'home.html', context)


def create_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        item = Item(name=name)
        item.save()
        return HttpResponse(f'<li class="text-8xl font-thin">{item.name}</li>')
    else:
        return redirect('home')  # Redirect to home if not a POST request