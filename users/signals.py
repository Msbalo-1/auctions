from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def createUser(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            full_name=user.first_name

        )


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_delete.connect(deleteUser, sender=Profile)


