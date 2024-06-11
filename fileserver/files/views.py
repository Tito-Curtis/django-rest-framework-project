from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from files.serializers import PersonSerializer
from files.models import Person

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
        return Response("This is a get method")
    def post(self, request):
        return Response("This is a post method")
    def put(self, request):
        return Response("This is a put method")
    def patch(self, request):
        return Response("This is a patch method")
    def delete(self, request):
        return Response("This is a delete method")