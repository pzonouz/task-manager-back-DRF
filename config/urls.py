from rest_framework.routers import SimpleRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from categories.views import CategoryViewSet

from django.contrib import admin
from django.urls import include, path, re_path

from priorities.views import PriorityViewSet
from tasks.views import TaskCompleteView, TaskViewSet

from users.views import JwtObtainPairView


urlpatterns = [
    path("api/v1/admin/", admin.site.urls),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns += [
    path("api/v1/tasks/<slug:id>/complete-task/", TaskCompleteView.as_view())
]
urlpatterns += [
    path("api/v1/auth/jwt/create/", JwtObtainPairView.as_view(), name="jwt_obtain_pair")
]
# TODO:Implement Logout
urlpatterns += [
    re_path("^api/v1/auth/", include("djoser.urls")),
    re_path("^api/v1/auth/", include("djoser.urls.jwt")),
]

router = SimpleRouter()
router.register(r"categories", CategoryViewSet, basename="Category")
router.register(r"priorities", PriorityViewSet, basename="Priority")
router.register(r"tasks", TaskViewSet, basename="Task")

urlpatterns += [path("api/v1/", include(router.urls))]
urlpatterns += [
    path(
        "api/v1/swagger<format>/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "api/v1/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "api/v1/redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
