from django.db import models

# Create your models here.
# full_name = models.CharField(max_length=100)
# location = models.CharField(max_length=100)
# phone_number = models.CharField(max_length=20)
# message = models.TextField()
# submitted_at = models.DateTimeField(auto_now_add=True)


from django.db import models

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, null=True)  # Optional
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created

    def __str__(self):
        return f"{self.full_name} - {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"
