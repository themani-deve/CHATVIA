from django.db import models
from Authentication.models import User


# Create your models here.


class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    message = models.CharField(max_length=999, null=True, blank=True)
    time = models.TimeField(auto_now_add=True, null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True, editable=False)

    def __str__(self):
        return f'{self.user} {self.message}'


class MlMessages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    message = models.CharField(max_length=999, null=True, blank=True)
    time = models.TimeField(auto_now_add=True, null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True, editable=False)

    def __str__(self):
        return f'{self.user} {self.message}'
