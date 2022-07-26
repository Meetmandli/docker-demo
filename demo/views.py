from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serilaizers import Student, StudentSerializer

class StudentDetails(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
