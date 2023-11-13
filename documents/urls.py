from django.urls import path, include
from documents import views

urlpatterns = [
    path('intern_schedule/', views.intern_schedule, name='intern_schedule'),
    path('enter_internship_info/', views.enter_internship_info, name='enter_internship_info'),
    path('view_internship_info/', views.view_internship_info, name='view_internship_info'),
    path('add_to_weekly_bin/<int:week_number>/', views.add_to_weekly_bin, name='add_to_weekly_bin'),
    path('add_weekly_bin/', views.add_weekly_bin, name='add_weekly_bin'),

    path('upload-requirements/', views.upload_requirements, name='upload_requirements'),
    path('upload-dtr/', views.upload_dtr, name='upload_dtr'),
    path('upload-narrative/', views.upload_narrative, name='upload_narrative'),
    path('upload-post-requirements/', views.upload_post_requirements, name='upload_post_requirements'),
    path('folder_list', views.folder_list, name='folder_list'),
    path('create_folder/', views.create_folder, name='create_folder'),
    path('folder/<int:folder_id>/', views.folder_detail, name='folder_detail'),

    path('delete-narrative/<str:narrative_number>/', views.delete_narrative, name='delete_narrative'),
    path('delete-dtr/<str:dtr_number>/', views.delete_dtr, name='delete_dtr'),

]
