from django.urls import path, include
from signup import views

urlpatterns = [
    path('create_intern/', views.intern_record, name='intern_record'),
]