from .views import ServiceAPIViewSet
from django.urls import re_path
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

schema_view = get_schema_view(
    openapi.Info(
        title="Your Project API",
        default_version='v1',
        description="API documentation",
    ),
    public=True,
    permission_classes=[permissions.IsAuthenticated],
)

router = DefaultRouter()
router.register(r'service', ServiceAPIViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="Music listening",
        default_version='v1',
        description="Music",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="<g-email>"),
        license=openapi.License(name="Listening"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', include(router.urls)),
    # path('swagger/', login_required(schema_view.with_ui('swagger', cache_timeout=0)), name='schema-swagger-ui'),
    # # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    # # path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]


