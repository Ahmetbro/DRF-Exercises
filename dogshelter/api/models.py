from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Breed(models.Model):
    DOG_SIZE = (
        ('T', 'tiny'),
        ('S', 'small'),
        ('M', 'medium'),
        ('L', 'large')
    )

    bname = models.CharField(max_length=250)
    size = models.CharField(max_length=50, choices=DOG_SIZE)
    friendliness = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    trainability = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    shedding_amount = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    exercise_needs = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return self.bname


class Dog(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='breed')
    gender = models.CharField(max_length=50)
    color = models.CharField(max_length=100)
    favorite_food = models.CharField(max_length=120)
    favorite_toy = models.CharField(max_length=120)

    def __str__(self):
        return self.name
        