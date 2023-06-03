from rest_framework import serializers
from task_manager.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class IndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title','description')        