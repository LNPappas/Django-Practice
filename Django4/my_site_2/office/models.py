from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MaxValueValidator(120), MinValueValidator(0)])
    heart_rate = models.IntegerField(default=60, validators=[MaxValueValidator(300), MinValueValidator(1)])
    
    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
