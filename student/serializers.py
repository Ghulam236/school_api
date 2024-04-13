from rest_framework import serializers
from .models import StudentUser,StuClass

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=StudentUser
        fields=['firstName','lastName','phone','email','password', 'dateOfBirth', 'status', 'image', 'cls']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        student = StudentUser.objects.create_user(**validated_data)
        return student

    def update(self, instance, validated_data):
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.lastName = validated_data.get('lastName', instance.lastName)
        instance.email = validated_data.get('email', instance.email)
        instance.dateOfBirth = validated_data.get('dateOfBirth', instance.dateOfBirth)
        instance.image = validated_data.get('image', instance.image)
        instance.cls = validated_data.get('cls', instance.cls)
        instance.save()
        return instance