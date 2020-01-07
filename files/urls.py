from django.urls import path, include

from . import views

app_name = 'files'

urlpatterns = [
    path('', views.petFiles_list, name='pets_list'),
    path('delete_file/', views.delete_file, name='delete_file'),

    path('add_pet/', views.add_pet, name='add_pet'),
    path('search_owners/', views.search_owners, name='search_owners'),

    path('<int:pk>/show_info/', views.pet_show_info, name='show_info'),
    path('<int:pk>/edit_info/', views.pet_edit_info, name='edit_info'),

    path('<int:pk>/clinic_history_list/',
         views.clinic_history_list, name='clinic_history_list'),
    path('delete_clinic_history/', views.delete_clinic_history,
         name='delete_clinic_history'),
    path('<int:pk>/new_clinic_history/',
         views.new_clinic_history, name='new_clinic_history'),

    path('<int:pk>/show_vaccination_history/',
         views.show_vaccination_history, name='show_vaccination_history'),

    path('<int:pk>/show_deworming_history/',
         views.show_deworming_history, name='show_deworming_history'),

    path('<int:pk>/show_internment_history/',
         views.show_internment_history, name='show_internment_history'),
]
