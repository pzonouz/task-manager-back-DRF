from rest_framework.serializers import ModelSerializer

from priorities.models import Priority


class PrioritySerializer(ModelSerializer):
    class Meta:
        model = Priority
        fields = "__all__"
