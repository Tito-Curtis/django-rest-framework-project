
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from files.views import ViewSet,ModelViewSet


router = DefaultRouter()
router.register("",ViewSet,basename="post_view_set")

model_router = DefaultRouter()
model_router.register("",ModelViewSet,basename="model_view_set")

urlpatterns = [
    path('', include('api.urls')),
    path('postview/', include(router.urls)),
    path('model_view/', include(model_router.urls)),
    path('auth/',include("account.urls")),
    path('admin/', admin.site.urls),
]
