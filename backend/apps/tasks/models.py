import uuid

from django.db import models
from apps.projects import models as project_models
from apps.users import models as user_models
# Create your models here.


class Task(models.Model):
    STATUS_CHOICES = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Script Testing', 'Script Testing'),
        ('Done', 'Done'),
        ('Backlog', 'Backlog'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sprint = models.ForeignKey(project_models.Sprint, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='To Do')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='Medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name='tasks', blank=True, null=True)

    def __str__(self):
        return self.title


class TaskAssignee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='assignees')
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name='assigned_tasks')
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} assigned to {self.task.title}'


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name='comentator')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment on {self.task.title}'
