from django.urls import path
from . import views

urlpatterns = [
    path('static_exaple/', views.static_exaple, name = 'static_exaple'),
    path('template_example/', views.template_example , name = 'template_example'),
    path('user_create/', views.user_create, name = 'user_create'),
    path('user_new/', views.user_new, name = 'user_new'),
    path('pong/', views.pong, name='pong'),
    path('ping/', views.ping, name='ping'),
    path('cube/<number>/', views.cube, name = 'cube'),
    path('hello/<name>/', views.hello, name='hello'),
    path('dinner/',views.dinner, name = 'dinner'),
    path('index/', views.index, name='index'),
]