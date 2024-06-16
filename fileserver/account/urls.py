from django.urls import path
from . import views

urlpatterns=[
    path('get_csrf/',views.GetCSRFView.as_view(),name='csrf_token'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
]