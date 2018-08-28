from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField(default='0')
    comment = models.CharField(max_length=1600, default='')
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender = models.CharField(
        max_length=1,
        choices=gender_choices,
        default='O'
    )

    def __str__(self):
        return self.name
