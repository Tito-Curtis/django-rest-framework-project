from rest_framework.response import Response
from rest_framework import status,generics,mixins,permissions,viewsets
from rest_framework.views import APIView
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate
from rest_framework.request import Request
from .serializers import SignUpSerializer,UserSerializer
from .models import CustomUser
from .tokens import create_jwt_pair_for_user


# Create your views here.
class GetCSRFView(APIView):
    def get(self, request, *args, **kwargs):
        csrf_token = get_token(request)
        return Response(data={"csrf_token": csrf_token}, status=status.HTTP_200_OK)
    
class SignUpView(generics.GenericAPIView,mixins.CreateModelMixin):
    serializer_class = SignUpSerializer
    permission_classes =[permissions.AllowAny]
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response={
                "message":"User created successfully",
                "data": serializer.data
            }
            return Response(data= response, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class GetAllUsers(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes =[permissions.AllowAny]
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        user = authenticate(email=email,password=password)
        if user is not None:
            response={
                "message":"User logged in successfully",
                "tokens": create_jwt_pair_for_user(user)
            }
            return Response(data=response,status=status.HTTP_200_OK)
        else:
            return Response(data={"message":"Invalid email or password"})
    def get(self,request):
        permission_classes =[permissions.IsAuthenticated]
        content = {
            "user":str(request.user),
            "auth":str(request.auth)
        }
        return Response(data=content,status=status.HTTP_200_OK)
