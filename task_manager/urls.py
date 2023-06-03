from django.urls import path
from .views import TaskListView


urlpatterns = [
    path('',TaskListView.as_view(template_name = 'TASSK/task_test.html')),
   
  ]