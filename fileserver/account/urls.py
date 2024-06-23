from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from . import views

urlpatterns=[
    path('get_csrf/',views.GetCSRFView.as_view(),name='csrf_token'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('jwt/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('user/',views.GetAllUsers.as_view({'get': 'list'}),name='user')
]