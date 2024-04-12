from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import StudentSerializer
from .models import Student_User,Stu_Class
# Create your views here.
@api_view(['POST'])
def register_student(request):
    data = request.data
    serializer = StudentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Student registered successfully.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_student(request):
    phone = request.data.get('phone')
    password = request.data.get('password')
    student = authenticate(request, username=phone, password=password)
    if student:
        if student.status:  # Check if student is active
            refresh = RefreshToken.for_user(student)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Account not activated.'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_student_profile(request):
    student = request.user
    serializer = StudentSerializer(student, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Profile updated successfully.'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)