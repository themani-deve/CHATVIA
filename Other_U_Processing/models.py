from django.db import models
from Authentication.models import User

# Create your models here.


class PermissionForDecodingModel(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user2')

    def __str__(self):
        return f'User 1: {self.user1}, User 2: {self.user2}'

    class Meta:
        unique_together = ('user1', 'user2')
