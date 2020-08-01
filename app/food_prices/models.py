import uuid

import django.utils.timezone
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from datetime import datetime

TODAY = datetime.today()


class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    snapshot = models.DateField(default=django.utils.timezone.now)
    country = models.CharField(max_length=50)
    price = models.FloatField(max_length=10)
    item = models.CharField(max_length=100)

    def __str__(self):
        return self.country


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
