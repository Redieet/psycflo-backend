from django.db import models

# Create your models here.
# user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
# message = models.TextField()
# response = models.TextField()
# timestamp = models.DateTimeField(auto_now_add=True)

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()  # Ensures compatibility with custom user models

class UserMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    response = models.TextField(blank=True)  # Allows response to be optional
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically sets when created

    def __str__(self):
        return f"Message from {self.user.username if self.user else 'Anonymous'} at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
