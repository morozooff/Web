
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('first', views.first, name = 'first'),
    path('second', views.second, name = 'second'),
    path('third', views.third, name = 'third'),
    path('reg', views.reg, name = 'reg'),
    path('create_comment/', views.create_comment),
    path('get_comments/', views.get_comments),
]

