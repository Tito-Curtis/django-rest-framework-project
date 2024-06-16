from rest_framework.response import Response
from rest_framework import status,generics,mixins
from rest_framework.views import APIView
from django.middleware.csrf import get_token
from .serializers import SignUpSerializer
from .models import CustomUser


# Create your views here.
class GetCSRFView(APIView):
    def get(self, request, *args, **kwargs):
        csrf_token = get_token(request)
        return Response(data={"csrf_token": csrf_token}, status=status.HTTP_200_OK)
    
class SignUpView(generics.GenericAPIView,mixins.CreateModelMixin):
    serializer_class = SignUpSerializer
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
    def get(self,request):
        obj = CustomUser.objects.all()
        serializer = SignUpSerializer(obj,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
