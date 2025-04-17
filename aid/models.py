from django.db import models

# Create your models here.
class AidRequest(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    requested_at=models.DateTimeField(auto_now_add=True)
    country=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    local_govrernment=models.CharField(max_length=30)
   

    def __str__(self):
        return f"{self.id} {self.fullname}"

class donors(models.Model):
    id=models.AutoField(primary_key=True)
    brandname=models.CharField(max_length=30)
    message=models.TextField()
    donated_at=models.DateTimeField(auto_now_add=True)
    distributed=models.DateTimeField(auto_now_add=True)
    website=models.URLField(blank=True)

    def __str__(self):
        return f"{self.brandname} {self.donated_at}"
    
    
