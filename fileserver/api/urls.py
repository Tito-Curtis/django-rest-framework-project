from files.views import index,person
from django.urls import path


urlpatterns = [
    path('', index),
    path('person/',person)
]