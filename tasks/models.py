from django.db import models


class Task(models.Model):
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

    def __str__(self):
        return self.name
