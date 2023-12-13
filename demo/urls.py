from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .api_router import CustomDefaultRouter
#from stores.views import StoreViewSet
from stores.views import StoreHoursViewSet, store_list,store_detail,CustomAuthTokenLogin


router = CustomDefaultRouter()
#router.register("stores", StoreViewSet, basename="stores")
router.register("storeHours", StoreHoursViewSet, basename="storesHours")


# Swagger documentation setup
schema_view = get_schema_view(
    openapi.Info(
        title="FoodTracks API",
        default_version='v1',
        description="FoodTracks Demo Documentation",
        terms_of_service="#",
        contact=openapi.Contact(email="contact@foodtracks.net"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/login/",CustomAuthTokenLogin.as_view(),name='login'),
    path("api/", include(router.urls)),
    path('api/stores/', store_list),
    path('api/stores/<uuid:id>', store_detail),
    re_path(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Foodtracks Super Admin"
admin.site.site_title = "Foodtracks"
admin.site.index_title = "Foodtracks Super Admin"