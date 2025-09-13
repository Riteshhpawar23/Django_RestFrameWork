from rest_framework import serializers
from Rest_main import stuff
from parents.models import Parents



class ParentsSerializer(serializers.ModelSerializer):

    class Meta:
        model= Parents
        fields='__all__'