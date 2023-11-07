from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_homepage, name='index'),
    path("createContact", views.index, name='Contact'),
    path('contacts/', views.display_contacts, name='contact_list'),
    path('user/<int:user_id>/', views.delete, name='delete'),
    path('update_contact/<int:user_id>/',
         views.update_contact, name='update_contact'),
]
