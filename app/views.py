from django.shortcuts import render
from rest_framework import generics

# Create your views here.

from .models import Owner, student
from .serializers import UserSerial, studentserial


class CreateListUserView(generics.ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = UserSerial
    print(queryset)
  
        
class GetByIDUserView(generics.RetrieveAPIView):
    queryset = Owner.objects.all()
    serializer_class = UserSerial
    def perform_create(self , serializer):
        serializer.save()
    
    
class UpdateUserView(generics.UpdateAPIView):
    queryset = Owner.objects.all()
    serializer_class = UserSerial
    look_up = "pk"


class DeleteUserView(generics.DestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = UserSerial
    look_up = "pk"
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        
class CreateListStudentView(generics.ListCreateAPIView):
    queryset = student.objects.all()
    serializer_class = studentserial
    print(queryset)      
        