from django.db import models

# Create your models here.
class Todo(models.Model):
	text =models.CharField(max_length=40)
	completed=models.BooleanField (default=False)