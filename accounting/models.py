from django.db import models

from django.contrib.auth.models import User

class CustomUser(models.Model):
    image=models.ImageField(blank=True, upload_to='user_profile', default='user_profile/download.jfif')
    name=models.CharField(max_length=40, blank=True, null=True)
    last_name=models.CharField(max_length=40, blank=True, null=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    GENDERS = (
        ('M', 'Male'),
        ("F", 'Female'),
    )
    age=models.PositiveIntegerField(null=True)
    gender=models.CharField(max_length=10, choices=GENDERS, null=True)
    national_code=models.CharField(max_length=20, null=True)
    phone_number=models.PositiveBigIntegerField(null=True)
    email=models.EmailField(blank=True, null=True)
    addres=models.TextField(null=True)
    debt=models.OneToOneField("loan.Debt", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user.username}'

