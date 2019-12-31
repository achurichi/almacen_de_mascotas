from django.urls import path, include

from . import views

app_name = 'files'

urlpatterns = [
    path('', views.petFiles_list, name='pets_list'),
    path('delete_file/', views.delete_file, name='delete_file'),
    path('add_pet/', views.add_pet, name='add_pet'),
    path('search_owners/', views.search_owners, name='search_owners'),
    path('<int:pk>/', views.pet_file_detail, name='detail'),
    path('edit_file/', views.edit_file, name="edit_file"),
]
