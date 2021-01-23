from django.db import models

# Create your models here.
class Add_ewaste(models.Model):
    Name = models.CharField(max_length=120)
    Surname = models.CharField(max_length=120)
    Ward = models.PositiveIntegerField()
    Mob_number = models.PositiveBigIntegerField()
    Email = models.CharField(max_length=120)
    Address = models.TextField()
    Image = models.ImageField(upload_to='images/')
