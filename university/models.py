from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=250)
    logo = models.TextField()
    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=250)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Application(models.Model):
    ACCEPTED = 'AC'
    PENDING = 'PE'
    REJECTED = 'RE'
    DEFERRED = 'DE'
    STATUS_CHOICES = [
        (ACCEPTED, 'Accepted'),
        (PENDING, 'Pending'),
        (REJECTED, 'Rejected'),
        (DEFERRED, 'Deferred'),
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PENDING)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, default=None)
    grade = models.IntegerField(default=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)