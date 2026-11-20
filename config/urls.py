
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Auth Service API",
        default_version='v1',
        description="API documentation for authentication microservice",
        contact=openapi.Contact(email="admin@example.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


def home(request):
    return JsonResponse({
        "message": "Welcome to Auth Service!",
        "status": "working",
    })


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),

    path('api/auth/', include('users.urls')),

    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),

    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]
