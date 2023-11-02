from django.urls import path, include
from documents import views

urlpatterns = [
    path('intern_schedule/', views.intern_schedule, name='intern_schedule'),
    path('enter_internship_info/', views.enter_internship_info, name='enter_internship_info'),
    path('view_internship_info/', views.view_internship_info, name='view_internship_info'),
    path('add_to_weekly_bin/<int:week_number>/', views.add_to_weekly_bin, name='add_to_weekly_bin'),
    path('add_weekly_bin/', views.add_weekly_bin, name='add_weekly_bin'),
]