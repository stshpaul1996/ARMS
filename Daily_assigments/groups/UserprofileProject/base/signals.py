from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile,Role


@receiver(post_save, sender=User)
def user_saved(sender, instance, created, **kwargs):
    if created:
        role_id = 1
        role_inst = Role.objects.get(id=role_id)
        UserProfile.objects.create(user=instance, role=role_inst)

