from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Django's AbstractUser already provides fields like username, email, password, etc.
    # created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username
    

