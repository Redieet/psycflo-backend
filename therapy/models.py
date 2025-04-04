from django.db import models

# Create your models here.
# user = models.ForeignKey(User, on_delete=models.CASCADE)
# preferred_time = models.DateTimeField()
# # session_type  e.g., "online" or "in-person"
# session_type = models.CharField(max_length=20)  
# notes = models.TextField()
# status = models.CharField(max_length=20, default="pending")

from django.contrib.auth import get_user_model  
from django.db import models  

User = get_user_model()  # Dynamically gets the User model  

class Session(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    preferred_time = models.DateTimeField()  
    session_type = models.CharField(max_length=20)  
    notes = models.TextField()  
    status = models.CharField(max_length=20, default="pending")  
