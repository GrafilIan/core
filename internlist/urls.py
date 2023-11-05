from django.urls import path
from . import views

urlpatterns = [
    path('intern_list', views.intern_list, name='intern_list'),
    path('interns/<int:intern_id>/', views.intern_detail, name='intern_detail'),
    path('admin_intern_detail/<int:intern_id>/', views.admin_intern_detail, name='admin_intern_detail'),
    path('view_requirements/<int:intern_id>/', views.view_requirements, name='view_requirements'),
    path('view_dtr/<int:intern_id>/', views.view_dtr, name='view_dtr'),
    path('view_post_requirements/<int:intern_id>/', views.view_post_requirements, name='view_post_requirements'),
    path('view_weekly_report/<int:intern_id>/', views.view_weekly_report, name='view_weekly_report'),

]
