from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_announcement, name='create_announcement'),
    path('intern_announcement_list/', views.intern_announcement_list, name='intern_announcement_list'),
    path('announcement_list/', views.announcement_list, name='announcement_list'),
    path('delete_item/<str:item_type>/<int:item_id>/', views.delete_item, name='delete_item'),
]