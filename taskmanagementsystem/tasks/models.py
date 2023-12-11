from django.db import models
from task_categories.models import TaskCategory

# Create your models here.

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=255)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssignDate = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(TaskCategory)

    def __str__(self):
        return f"{self.taskTitle}"