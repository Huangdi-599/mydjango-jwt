from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.conf import settings

"""
Applying user data to the model, so each user with their data
"""

#User = settings.AUTH_USER_MODEL


""""
CREATING USER MODEL BY EXTENDING DJANGO USER MODEL
"""

class Owner(AbstractUser):
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255, unique = True)
    password = models.CharField(max_length = 255)
    username = models.CharField(max_length = 255, null = True)
    
    ##CHANGING LOGIN TO BE email instead of password
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    


""""
GO TO SETTINGS AND REGISTER AS
AUTH_USER_MODEL = 'users.User'

"""


class student(models.Model):
    name = models.CharField(max_length=500)
    age = models.IntegerField()
    description = models.TextField()
    date_enrolled = models.DateField(auto_now= True)

    def _str_(self):
        return self.name