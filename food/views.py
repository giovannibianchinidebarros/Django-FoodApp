from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Create your views here.


def hello(request):
    return HttpResponse('Hello world')


# def index(request):
#     item_list = Item.objects.all()
#     template = loader.get_template('food/index.html')
#     context = {
#         'item_list': item_list,
#     }
#     return HttpResponse(template.render(context, request))


# def index(request):
#     context = {
#         'item_list': Item.objects.all(),
#     }
#     return render(request, 'food/index.html', context)

class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'


# def detail(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     context = {
#         'item': item,
#     }
#     return render(request, 'food/detail.html', context)

class FoodDetailClassView(DetailView):
    model = Item
    template_name = 'food/detail.html'


# def create_item(request):
#     form = ItemForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         return redirect('food:index')

#     return render(request, 'food/item-form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)


def update_item(request, item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)

    context = {
        'form': form,
        'item': item,
    }

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', context)


def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)

    if request.method == 'POST':
        if "confirm_button" in request.POST:
            item.delete()
        return redirect('food:index')

    return render(request, 'food/item-delete.html', {'item': item})
