from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from menu.models import Drink, Coffee, BubbleTea


class DrinkListView(ListView):
    model = Drink
    #paginate_by = 3


class CoffeeCreateView(CreateView):
    model = Coffee
    fields = ['name', 'price', 'image'] #'__all__'
    template_name = 'menu/coffee_create.html'
    success_url = reverse_lazy('menu:list')
    initial = {'category': 'Coffee'}


class BubbleTeaCreateView(CreateView):
    model = BubbleTea
    fields = '__all__'  # ['category', 'name', 'price', 'image']
    template_name = 'menu/drink_create.html'
    success_url = reverse_lazy('menu:list')
    initial = {'category': 'BubbleTea'}


class DrinkUpdateView(UpdateView):
    model = Drink
    fields = '__all__'
    template_name_suffix = '_update'  # drink_update.html
    success_url = reverse_lazy('menu:list')


class DrinkDeleteView(DeleteView):
    model = Drink
    success_url = reverse_lazy('menu:list')

