from rest_framework.viewsets import ModelViewSet
from priorities.models import Priority
from priorities.serializers import PrioritySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PriorityViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
