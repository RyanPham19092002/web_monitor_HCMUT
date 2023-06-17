from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    def __str__(self):
        return self.username
class Pass(models.Model):
    passuser = models.ForeignKey(User, on_delete = models.CASCADE)
    password = models.CharField(max_length=300)
    def __str__(self):
        return self.password
class Email(models.Model):
    emailuser = models.ForeignKey(User, on_delete = models.CASCADE)
    email = models.CharField(max_length=300)
    def __str__(self):
        return self.email