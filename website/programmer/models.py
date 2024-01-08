from django.db import models
from django.conf import settings


class Portfolio(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='images/')

    education = models.TextField()
    qualities = models.TextField()
    abilities = models.TextField()
    awards = models.TextField()

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
