from rest_framework.routers import SimpleRouter

from categories.views import CategoryViewSet

from django.contrib import admin
from django.urls import path

from priorities.views import PriorityViewSet
from tasks.views import TaskViewSet

urlpatterns = [
    path("admin/", admin.site.urls),
]


router = SimpleRouter()
router.register(r"categories", CategoryViewSet, basename="Category")
router.register(r"priorities", PriorityViewSet, basename="Priority")
router.register(r"tasks", TaskViewSet, basename="Task")

urlpatterns = []
urlpatterns = urlpatterns + router.urls
