from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.Home, name='home'),
    path('product/<str:slug>', views.Detail, name='detail'),
    path('contact/', views.Contact, name='contact'),
]