from django.db import models
from django.utils import timezone

class Enrollment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField()
    course = models.CharField(max_length=255)
    info = models.TextField()
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField()
    message = models.TextField()
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
class Testimony(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    course = models.CharField(max_length=255)
    message = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name