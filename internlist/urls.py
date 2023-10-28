from django.urls import path
from . import views

urlpatterns = [
    path('intern_list', views.intern_list, name='intern_list'),
    ]