from django.urls import path
from .views import AllTaskView,TaskDetailView,TaskCreateAPIView,TaskUpdateView,TaskDelete


urlpatterns = [
   path('',AllTaskView.as_view(), name='task_all_view'),
   path('task_detail/<int:pk>/',TaskDetailView.as_view(), name='task_detail'),
   path('create/',TaskCreateAPIView.as_view(),name='create-task'),
   path('update/<int:pk>/',TaskUpdateView.as_view(),name='update-task'),
   path('delete/<int:pk>/',TaskDelete.as_view(),name='delete-task'),
   # path('tasks/', TaskList.as_view(), name='task-list'),

  ]

