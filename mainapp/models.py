from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"  

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='profile', on_delete=models.CASCADE)
    role = models.ForeignKey(Role)
    def __unicode__(self):
        return self.user.username
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles" 

class Visitor(models.Model):
    name = models.CharField(max_length=20)
    cedula = models.CharField(max_length=20)
    #goesToVisit = models.ChoiceField()
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Visitor"
        verbose_name_plural = "Visitos"