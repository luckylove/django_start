from django.db.models.signals import post_save
from django.contrib.auth.models import User
# user model is sending the signal
# so we want some reciever who will recieve the signals send by the user sender
from django.dispatch import receiver
from .models import Profile


# it indicates when the user is created it send the post save signal
# so if signal is present
# **kwargs is used to accept any other remaining parameter left at the end


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


