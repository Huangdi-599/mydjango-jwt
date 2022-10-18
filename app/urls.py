from django.urls import path
from . import views

urlpatterns = [
    
    
    path('student', views.CreateListStudentView.as_view()),
    path('user', views.CreateListUserView.as_view()),
    path('school', views.CreateListSchoolView.as_view()),
    path('create', views.CreateStudentView.as_view()),
    #path('user/login', views.LoginMixin.as_view()),
    #path('user/logout', views.LogoutView.as_view()),
    path('user/<int:pk>', views.GetByIDUserView.as_view()),
    path('user/<int:pk>/delete', views.DeleteUserView.as_view()),
    path('user/<int:pk>/update', views.UpdateUserView.as_view())

   
]