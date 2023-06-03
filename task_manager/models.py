from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status_choices = (
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    )
    status = models.CharField(max_length=20, choices=status_choices)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
