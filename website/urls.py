from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),

    path('pets/', views.pet_list, name='pets'),

    path('services/', views.services, name='services'),

    path('register/', views.register, name='register'),

    path('login/', views.login, name='login'),

    path('adopt/', views.adopt_pet, name='adopt'),

    path(
        'book-grooming/',
        views.book_grooming,
        name='book_grooming'
    ),
    path(
    'feedback/',
    views.feedback_page,
    name='feedback'
    ),
    path(
    'notifications/',
    views.notifications_page,
    name='notifications'
    ),
    path(
    'dashboard/',
    views.dashboard,
    name='dashboard'
   ),
   path(
    'logout/',
    views.logout_user,
    name='logout'
),
path(
    'message/',
    views.message_page,
    name='message'
),
]