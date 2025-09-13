from .serializers import StudentSerializer,teacherSerializer,stuffSerializer,ParentsSerializer
from rest_framework.response import Response
from Students.models import Student
from teacher.models import teacher
from stuff.models import Stuff
from parents.models import Parents
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics, mixins



@api_view(['GET','POST'])
# Create your views here.
def studentview(request):
    if request.method=='GET':
        student=Student.objects.all()
        serializer=StudentSerializer(student,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)   
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

@api_view(['GET','PUT','DELETE'])
def studentdetailview(request,pk):
    try:
        student=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method=='PUT':
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class Teacher(APIView):
    def get(self, request):
        teachers = teacher.objects.all()
        serializer = teacherSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
     
     
    def post(self, request):
        serializer = teacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Teacherdetail(APIView):
    def get_object(self,pk):
        try:
            return teacher.objects.get(pk=pk)
        except teacher.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
            teacher_instance = self.get_object(pk)
            serializer = teacherSerializer(teacher_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)   
        
    def put(self, request, pk):
            teacher_instance = self.get_object(pk)
            serializer = teacherSerializer(teacher_instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
            teacher_instance = self.get_object(pk)
            teacher_instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
class StuffListCreateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Stuff.objects.all()
    serializer_class = stuffSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
class StuffDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Stuff.objects.all()
    serializer_class = stuffSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
    

class ParentsListCreateView(generics.ListCreateAPIView):
    queryset = Parents.objects.all()
    serializer_class = ParentsSerializer
 
class ParentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parents.objects.all()
    serializer_class = ParentsSerializer
    lookup_field = 'pk'