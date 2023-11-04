from django.urls import path
from . import views

urlpatterns = [
    path('intern_list', views.intern_list, name='intern_list'),
    path('interns/<int:intern_id>/', views.intern_detail, name='intern_detail'),
    ]