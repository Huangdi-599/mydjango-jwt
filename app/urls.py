from django.urls import path
from . import views

urlpatterns = [
    
    
    path('', views.CreateListStudentView.as_view()),
    path('user', views.CreateListUserView.as_view()),
    path('user/<int:pk>', views.GetByIDUserView.as_view()),
    path('user/<int:pk>/delete', views.DeleteUserView.as_view()),
    path('user/<int:pk>/update', views.UpdateUserView.as_view())

   
]