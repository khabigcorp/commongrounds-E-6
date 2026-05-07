from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .services import create_profile_for_user


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        create_profile_for_user(user=instance, display_name=instance.username)
