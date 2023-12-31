from django.urls import path, include
from signup import views
from documents.views import intern_schedule

urlpatterns = [
    path('add_intern_records/', views.add_intern_records, name='add_intern_records'),
    path('intern_schedule/', intern_schedule, name='intern_schedule'),
    path('edit_intern_status/<int:intern_id>/', views.edit_intern_status, name='edit_intern_status'),
]
