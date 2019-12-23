from django.urls import path, include

from . import views

app_name = 'files'

urlpatterns = [
    path('', views.petFiles_list, name='pets_list'),
    path('add_pet/', views.add_pet, name='add_pet'),
]
