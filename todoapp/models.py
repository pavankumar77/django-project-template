from django.db import models
from django.contrib.auth.models import User
from django import forms


class Tasks(models.Model):
    
    user_name = models.ForeignKey(User)
    task_name = models.CharField(max_length=50)
    task_accessibility = models.CharField(max_length=50)
    task_status = models.CharField(max_length=50)
    due_date = models.DateTimeField()
    
    
    
    def __unicode__(self):
        return self.task_name



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')



# Create your models here.
