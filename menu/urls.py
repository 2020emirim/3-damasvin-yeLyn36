from django.urls import path

from menu.views import DrinkListView, CoffeeCreateView, BubbleTeaCreateView, DrinkUpdateView, DrinkDeleteView

app_name = 'menu'

urlpatterns = [
    path('', DrinkListView.as_view(), name="list"),
    path('add_bubbletea', BubbleTeaCreateView.as_view(), name="add_bubbletea"),
    path('add_coffee', CoffeeCreateView.as_view(), name="add_coffee"),
    path('update/<int:pk>/', DrinkUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', DrinkDeleteView.as_view(), name="delete"),
]