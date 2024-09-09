from rest_framework.viewsets import ModelViewSet
from priorities.models import Priority
from priorities.serializers import PrioritySerializer


class PriorityViewSet(ModelViewSet):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
