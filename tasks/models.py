from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid


class Task(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    priority = models.ForeignKey(
        "priorities.Priority", on_delete=models.CASCADE, related_name="tasks"
    )
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="tasks"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="tasks"
    )
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    progress_percentage = models.IntegerField(
        default=0, validators=[MaxValueValidator(100), MinValueValidator(0)]
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        self.description = self.description.lower()
        if self.progress_percentage == 100:
            self.completed = True
        if self.progress_percentage < 100:
            self.completed = False
        super(Task, self).save(*args, **kwargs)
