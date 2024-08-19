from .models import Mentor, Service

from rest_framework import serializers

class MentorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'age', 'working', 'level')


class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('title', 'description', 'mentor')
