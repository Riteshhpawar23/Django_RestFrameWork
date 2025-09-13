from rest_framework import serializers
from stuff.models import stuff



class stuffSerializer(serializers.ModelSerializer):

    class Meta:
        model= stuff
        fields='__all__'