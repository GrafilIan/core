from django.urls import path, include
from signup import views

urlpatterns = [
    path('add_intern_records/', views.add_intern_records, name='add_intern_records'),

]
