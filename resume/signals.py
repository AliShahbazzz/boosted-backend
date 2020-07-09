from django.db.models.signals import post_save
from django.dispatch import receiver
from .serializers import ResumePropertySerializer
from .models import *


@receiver(post_save, sender=UserResume)
def create_property(sender, instance, created, **kwargs):
    if created:
        # resumeProp = ResumePropertySerializer(data=instance)
        ResumeProperties.objects.create(resume=instance)
        print(instance)


@receiver(post_save, sender=UserResume)
def save_property(sender, instance, **kwargs):
    instance.resumeproperties.save()
