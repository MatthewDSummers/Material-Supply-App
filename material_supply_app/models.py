from django.db import models
from login_app.models import User
# Create your models here.


class Material(models.Model):
    name = models.CharField(max_length=255)
    cost = models.IntegerField(blank=True, null=True)
    health = models.CharField(max_length=255, blank=True, null=True)
    flammability = models.CharField(max_length=255, blank=True, null=True)
    specificity = models.CharField(max_length=255, blank=True, null=True)
    instability = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = MaterialManager()

class Line(models.Model):
    name = models.CharField(max_length=255)
    material = models.ForeignKey(Material, related_name="lines", on_delete=models.CASCADE, blank=True, null=True)
    employee = models.ForeignKey(User, related_name="lines", on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = LineManager()

class Department(models.Model):
    name = models.CharField(max_length=255)
    line = models.ForeignKey(Line, related_name="departments", on_delete=models.CASCADE, blank=True, null=True)
    employee = models.ForeignKey(User, related_name="departments", on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = DepartmentManager()

