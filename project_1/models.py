from django.db import models

# Create your models here.

class User(models.Model):
    ROLES = (
        ('admin', 'Адміністратор'),
        ('user', 'Користувач'),
    )


    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=50, choices=ROLES)


