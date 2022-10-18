from django.shortcuts import render
from rest_framework import generics,authentication,permissions
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
import jwt, datetime
# Create your views here.

from .models import Owner, student,school
from .serializers import UserSerial, studentserial,schoolserial
from .permissions import IsStaffPermission,IsUserPermission






class CreateListUserView(generics.ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = UserSerial
    permission_classes = [permissions.IsAdminUser,IsStaffPermission]
    authentication_classes = [authentication.SessionAuthentication]
    print(queryset)
    def perform_create(self , serializer):
        serializer.save()
  
        
class GetByIDUserView(generics.RetrieveAPIView):
    queryset = Owner.objects.all()
    serializer_class = UserSerial
    permission_classes = [permissions.IsAdminUser,IsStaffPermission]
    authentication_classes = [authentication.SessionAuthentication]
    
    
    
class UpdateUserView(generics.UpdateAPIView):
    queryset = Owner.objects.all()
    serializer_class = UserSerial
    permission_classes = [permissions.IsAdminUser,IsStaffPermission]
    authentication_classes = [authentication.SessionAuthentication]
    look_up = "pk"
    

class DeleteUserView(generics.DestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = UserSerial
    permission_classes = [permissions.IsAdminUser,IsStaffPermission]
    authentication_classes = [authentication.SessionAuthentication]
    look_up = "pk"
    
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        
        
"""
Student Class Based Views
"""       
        
        
class CreateListStudentView(generics.ListAPIView):
    queryset = student.objects.all()
    serializer_class = studentserial
    print(queryset) 
    
         
    
class CreateStudentView(generics.CreateAPIView):
    queryset = student.objects.all()
    serializer_class = studentserial
    permission_classes = [permissions.IsAdminUser,IsStaffPermission]
    authentication_classes = [authentication.SessionAuthentication]
    print(queryset)       
    
    
    
        
"""
School Class Based Views
"""
class CreateListSchoolView(generics.ListCreateAPIView):
    queryset = school.objects.all()
    serializer_class = schoolserial
    permission_classes = [IsUserPermission]
    authentication_classes = [authentication.SessionAuthentication]
    print(queryset)
    def perform_create(self , serializer):
        user= self.request.user
        print(user)
        serializer.save(user= user)
    
    def get_queryset(self, *args , **kwargs):
        qs = super().get_queryset(*args , **kwargs)
        request  = self.request
        user = request.user
        if user.is_authenticated:
            return qs.filter(user= request.user)
        
        
"""       
  A simple jwt login and logout views
"""           
        
#class LoginMixin(generics.GenericAPIView):
#    queryset = Owner.objects.all()
#    serializer_class = UserSerial
#    def post (self, request, *args, **kwargs):
#        email = request.data['email']
#        password = request.data['password']
#        user = Owner.objects.filter(email=email).first()
#        print(user)
#        if user is None:
#            raise AuthenticationFailed("User not found")
#        if not user.check_password(password):
#            raise AuthenticationFailed("Incorrect Password")
#        
#        """
#        Setting JWT PAYLOAD
#        """
#        payload = {
#            'userid' : user.id,
#            'exp' : str(datetime.datetime.utcnow() + datetime.timedelta(minutes = 60)),
#            'lat' :str(datetime.datetime.utcnow())
#        }
#        
#        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
#        
#        """
#        saving the token as a cookie
#        """
#        response = Response()
#        response.set_cookie(key='jwt', value=token, httponly=True)
#        response.data = {          
#            'messages' : 'Login Successful',
#            'token' : token
#            }
#        return response
#        
#class UserView(generics.GenericAPIView):
#    def get(self, request, *args, **kwargs):
#        token = request.COOKIES.get('jwt')
#        if not token:
#            raise AuthenticationFailed('Unauthenticated !')
#        
#        try:
#            payload = jwt.decode(token, 'secret', alogrithm =['HS256'])
#        except jwt.ExpiredSignatureError:
#            raise AuthenticationFailed('Unauthenticated !')
#        """
#        Getting user from payload
#        """
#        user = Owner.objects.filter(id = payload['id'])
#        serializer = UserSerial(user)
#        return Response(serializer.data)
#    
#    
#class LogoutView(generics.GenericAPIView):
#    def post(self, request, *args, **kwargs):
#        response = Response()
#        response.delete_cookie('jwt')
#        response.data = {
#            'message': "Logout sucessful",
#            
#        }
#        return response
#                
#        