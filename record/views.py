from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Students, Course, Enrollment
from .serializers import StudentSerializer, CourseSerializer, EnrollmentSerializers

# Create your views here.


class StudentViewSet(viewsets.ModelViewSet):
     queryset = Students.objects.all()
     serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
     queryset = Course.objects.all()
     serializer_class = CourseSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
     queryset = Enrollment.objects.all()
     serializer_class = EnrollmentSerializers


























