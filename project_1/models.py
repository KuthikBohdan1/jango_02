from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class User(models.Model):
    ROLES = (
        ('admin', 'Адміністратор'),
        ('user', 'Користувач'),
    )




    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=50, choices=ROLES)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'