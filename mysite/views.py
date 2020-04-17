from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ItemForm
from .models import Item
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
#     item_list = Item.objects.all()
#     return render(request, 'mysite/index.html', {'item': item_list})
#
#
# def detailView(request, item_id):
#     item_view = Item.objects.get(pk=item_id)
#     return render(request, 'mysite/detail.html', {'item_view': item_view})

class MysiteDetail(DetailView):
    model = Item
    template_name = 'mysite/detail.html'
    context_object_name = 'item_view'


class IndexClassView(ListView):
    model = Item
    template_name = 'mysite/index.html'
    context_object_name = 'item'


# def create_item(request):
#     form = ItemForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('mysite:index')
#     return render(request, 'mysite/item-form.html', {'form': form})


class CreateItem(CreateView):
    model = Item
    fields = ['name', 'price', 'description', 'image']
    template_name = 'mysite/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('mysite:index')
    return render(request, 'mysite/item-form.html', {'form': form, 'item': item})


def delete_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('mysite:index')
    return render(request, 'mysite/item-delete.html', {'item': item})