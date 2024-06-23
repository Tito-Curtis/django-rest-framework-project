from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,mixins,generics,viewsets,permissions
from files.serializers import PersonSerializer,PostSerializer
from files.models import Person,Post
from django.shortcuts import get_object_or_404
from account.serializers import CurrentUserPostSerializer

@api_view(['GET'])
def index(request):
    course = {
        'course_name': 'Python',
        'course_content':['Django','Flask','Rest'],
        'instructor':'Curtis'
    }
    return Response(course)

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def person(request):
    if request.method == 'GET':
        obj = Person.objects.all()
        serializer = PersonSerializer(obj, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        user = Person.objects.get(id=data['id'])
        serializer = PersonSerializer(user,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'PATCH':
        data = request.data
        user = Person.objects.get(id=data['id'])
        serializer = PersonSerializer(user,data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'DELETE':
        data = request.data
        user = Person.objects.get(id=data['id'])
        user.delete()
        return Response(f"{user.name} deleted ") 
class ApiViewExample(APIView):
    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        response = {
            "message":"post",
            "data": serializer.data
        }
        return Response(response,status=status.HTTP_200_OK)
    def post(self, request):
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        return Response("This is a put method")
    def patch(self, request):
        return Response("This is a patch method")
    def delete(self, request):
        return Response("This is a delete method")
@api_view(["GET"])
def post_id(request,post_id=None):
    if post_id:
        obj = get_object_or_404(Post,id=post_id)
        serializer = PostSerializer(obj)
        print(obj)
    else:
        obj = Post.objects.all()
        serializer = PostSerializer(obj,many=True)
    return Response(serializer.data)

class PostViewSet(generics.GenericAPIView,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin):
                  
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        user = self.request.user
        print(f"User is: {user}")
        serializer.save(author=user)
        
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)   
class DeleteRetrieveUpdate(generics.GenericAPIView,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ViewSet(viewsets.ViewSet):
    def list(self,request):
        post = Post.objects.all()
        serializer = PostSerializer(instance=post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def retrieve(self,request,pk=None):
        queryset = get_object_or_404(Post,pk=pk)
        serializer = PostSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_by_post(request):
    user = request.user
    serializer = CurrentUserPostSerializer(instance=user)
    return Response(serializer.data, status=status.HTTP_200_OK)
