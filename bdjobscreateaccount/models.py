from django.db import models

# Create your models here.

class Skills(models.Model):
    name = models.CharField(max_length = 200)
     
    def __str__(self):
        return self.name

class Country(models.Model):
    country_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.country_name

GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

USER_ID = (
    ('email', 'Email'),
    ('phone', 'Phone'),
)


class UserRegistration(models.Model):
    name = models.CharField(max_length = 255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    skills = models.ForeignKey(Skills, on_delete=models.CASCADE)
    email = models.EmailField()
    mobile_number = models.CharField(max_length = 11)
    user_id = models.CharField(max_length=10, choices=USER_ID)
    password = models.CharField(max_length = 100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
    
  