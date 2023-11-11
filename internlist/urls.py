from django.urls import path

from documents.views import folder_list, create_folder, folder_detail
from signup.views import edit_intern_status
from . import views


urlpatterns = [
    path('intern_list', views.intern_list, name='intern_list'),
    path('interns/<int:intern_id>/', views.intern_detail, name='intern_detail'),
    path('admin_intern_detail/<int:intern_id>/', views.admin_intern_detail, name='admin_intern_detail'),
    path('view_requirements/<int:intern_id>/', views.view_requirements, name='view_requirements'),
    path('view_dtr/<int:intern_id>/', views.view_dtr, name='view_dtr'),
    path('view_post_requirements/<int:intern_id>/', views.view_post_requirements, name='view_post_requirements'),
    path('view_weekly_report/<int:intern_id>/', views.view_weekly_report, name='view_weekly_report'),
    path('intern_list/<int:intern_id>/', views.intern_list, name='intern_list'),
    path('folder_list',folder_list, name='folder_list'),
    path('create_folder/', create_folder, name='create_folder'),
    path('folder/<int:folder_id>/', folder_detail, name='folder_detail'),
    path('archive_intern/<int:intern_id>/<int:folder_id>/', views.archive_intern, name='archive_intern'),
    path('archive_selected_interns/', views.archive_selected_interns, name='archive_selected_interns'),


]
