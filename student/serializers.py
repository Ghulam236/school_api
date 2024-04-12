from rest_framework import serializers
from .models import Student_User,Stu_Class

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Student_User
        fields=['firstName','lastName','phone','email','password', 'dateOfBirth', 'status', 'image', 'clas']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        student = Student_User.objects.create_user(**validated_data)
        return student

    def update(self, instance, validated_data):
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.lastName = validated_data.get('lastName', instance.lastName)
        instance.email = validated_data.get('email', instance.email)
        instance.dateOfBirth = validated_data.get('dateOfBirth', instance.dateOfBirth)
        instance.image = validated_data.get('image', instance.image)
        instance.clas = validated_data.get('clas', instance.clas)
        instance.save()
        return instance