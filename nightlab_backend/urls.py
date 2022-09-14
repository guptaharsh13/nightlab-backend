from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from .views import index
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

admin.site.site_title = 'Nightlab'
admin.site.site_header = 'Nightlab Admin Panel'
admin.site.index_title = 'Welcome to Nightlab Admin Panel'


schema_view = get_schema_view(
    openapi.Info(
        title="Nightlab",
        default_version='v1.0.0',
        description="Nightlab Backend",
        contact=openapi.Contact(email=settings.DEFAULT_FROM_EMAIL)
    ),
    public=True,
    permission_classes=[AllowAny],

)

urlpatterns = [

    path('ieee/admin/', admin.site.urls),
    path("", view=index, name="index"),

    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),

]
