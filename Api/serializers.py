from rest_framework import serializers
from Students.models import Student 
from teacher.models import teacher
from stuff.models import Stuff

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' 

class teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacher
        fields = '__all__' 
        
class stuffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stuff
        fields = '__all__'