from django.db import models
from datetime import datetime
from django.utils import timezone


class SystemUser(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    email = models.EmailField(max_length=100, verbose_name="Email")
    contact_number = models.CharField(max_length=15, verbose_name="Contact Number")
    username = models.CharField(max_length=100, verbose_name="Username", unique=True)
    password = models.CharField(max_length=100, verbose_name="Password")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} ({self.username})"
