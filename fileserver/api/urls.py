from files.views import index,person,ApiViewExample
from django.urls import path


urlpatterns = [
    path('', index),
    path('person/',person),
    path('api_eg/',ApiViewExample.as_view())
]