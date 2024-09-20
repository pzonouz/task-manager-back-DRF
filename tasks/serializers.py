from categories.serializers import CategorySerializer
from tasks.models import Task
from rest_framework.serializers import ModelSerializer
from priorities.serializers import PrioritySerializer


class TaskSerializer(ModelSerializer):
    priority_obj = PrioritySerializer(source="priority", read_only=True)
    category_obj = CategorySerializer(source="category", read_only=True)

    class Meta:
        model = Task
        read_only_fields = ("priority_obj", "category_obj")
        fields = read_only_fields + (
            "id",
            "name",
            "description",
            "priority",
            "category",
            "user",
            "due_date",
            "created_at",
            "updated_at",
            "progress_percentage",
        )
