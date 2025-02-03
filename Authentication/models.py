from django.db import models
from django.contrib.auth.models import AbstractUser
import json


# Create your models here.


class User(AbstractUser):
    alphabet_dict = models.TextField(null=True, blank=True)

    def set_alphabet_dict(self, dictionary):
        self.alphabet_dict = json.dumps(dictionary)
        self.save()

    def get_alphabet_dict(self):
        return json.loads(self.alphabet_dict) if self.alphabet_dict else None
