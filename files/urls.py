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
    path('<int:pk>/show_clinic_history/<int:clinic_history_pk>/',
         views.show_clinic_history, name='show_clinic_history'),
    path('<int:pk>/edit_clinic_history/<int:clinic_history_pk>/',
         views.edit_clinic_history, name='edit_clinic_history'),

    path('<int:pk>/vaccination_history_list/',
         views.vaccination_history_list, name='vaccination_history_list'),
    path('delete_vaccination_history/', views.delete_vaccination_history,
         name='delete_vaccination_history'),

    path('<int:pk>/deworming_history_list/',
         views.deworming_history_list, name='deworming_history_list'),
    path('delete_deworming_history/', views.delete_deworming_history,
         name='delete_deworming_history'),


    path('<int:pk>/internment_history_list/',
         views.internment_history_list, name='internment_history_list'),
    path('delete_internment_history/', views.delete_internment_history,
         name='delete_internment_history'),
    path('<int:pk>/new_internment_history/',
         views.new_internment_history, name='new_internment_history'),
    path('<int:pk>/show_internment_history/<int:internment_history_pk>/',
         views.show_internment_history, name='show_internment_history'),
    path('delete_day_internment_history/', views.delete_day_internment_history,
         name='delete_day_internment_history'),
    path('add_day_internment_history/', views.add_day_internment_history,
         name='add_day_internment_history'),
    path('<int:pk>/show_day_internment_history/<int:internment_day_pk>/',
         views.show_day_internment_history, name='show_day_internment_history'),
    path('<int:pk>/edit_internment_history/<int:internment_history_pk>/',
         views.edit_internment_history, name='edit_internment_history'),
]
