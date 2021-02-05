from django.urls import path, include

from . import views

app_name = 'internment'

urlpatterns = [
    path('', views.internment_list, name='internment_list'),
    path('delete_internment/', views.delete_internment, name='delete_internment'),
]
