from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django.http import HttpResponseNotFound, HttpResponse

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all().order_by("created_at")
    serializer_class = TaskSerializer


class TaskCompleteView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            task = Task.objects.filter(id=kwargs.get("id")).first()
            if task is None:
                return HttpResponseNotFound({})
        except Exception:
            return HttpResponseNotFound({})
        task.completed = not task.completed
        task.save()
        return HttpResponse()
