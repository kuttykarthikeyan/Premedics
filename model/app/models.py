from django.db import models

# Create your models here.

class MediForm(models.Model):
  name = models.CharField(max_length=100, null=True)
  hospital_name = models.CharField(max_length=100, null=True)
  hospital_no = models.CharField(max_length=100)
  guardian_name = models.CharField(max_length=100, null=True)
  guardian_no = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
