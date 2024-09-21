from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify


class Task(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=300, unique=True)
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
    progress_percentage = models.IntegerField(
        default=0, validators=[MaxValueValidator(100), MinValueValidator(0)]
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        self.slug = slugify(self.name)
        self.description = self.description.lower()
        super(Task, self).save(*args, **kwargs)
