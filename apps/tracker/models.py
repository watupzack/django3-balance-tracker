from django.db import models
from django.contrib.auth.models import User


class UserBalance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mdl = models.IntegerField(default=0)
    eur = models.IntegerField(default=0)
    usd = models.IntegerField(default=0)
    ron = models.IntegerField(default=0)


    def __str__(self):
        return self.user.username + "'s balance"
