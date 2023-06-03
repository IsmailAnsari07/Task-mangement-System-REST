from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from task_manager.models import Task
from .serializers import TaskSerializer,IndividualSerializer
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
import django_filters.rest_framework



class AllTaskView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filterset_fields = ['title', 'due_date','status','assigned_to']


class TaskDetailView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = IndividualSerializer


class TaskCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all() 
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser, IsAuthenticated]

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class TaskUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'
    
class TaskDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    lookup_url_kwarg = 'pk'
    queryset = Task.objects.all()
    
# class TaskList(generics.ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
#     filterset_fields = ['title', 'due_date','status','assigned_to']
    




