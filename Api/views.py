from .serializers import StudentSerializer,teacherSerializer
from rest_framework.response import Response
from Students.models import Student
from teacher.models import teacher
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView



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
