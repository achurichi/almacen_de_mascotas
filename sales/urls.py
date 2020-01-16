from django.urls import path, include

from . import views

app_name = 'sales'

urlpatterns = [
    path('', views.products_list, name='products_list'),
    path('delete_product/', views.delete_product, name='delete_product'),
    path('<int:pk>/show_product/', views.show_product, name='show_product'),
    path('<int:pk>/edit_product/', views.edit_product, name='edit_product'),
]
