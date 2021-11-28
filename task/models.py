from django.db import models
from django.utils.translation import gettext_lazy


# Create your models here.
class Task(models.Model):

    class TaskStatus(models.TextChoices):
        TODO = 'todo', gettext_lazy('Todo')
        IN_PROGRESS = 'in_progress', gettext_lazy('In Progress')
        CLOSED = 'closed', gettext_lazy('Closed')
        CANCELED = 'canceled', gettext_lazy('Canceled')

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.TODO,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tasks'
