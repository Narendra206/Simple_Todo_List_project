from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('delete/<int:task_id>/', views.delete_task, name='delete'),
    path('complete/<int:task_id>/', views.mark_complete, name='complete'),

]
