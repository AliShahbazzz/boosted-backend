from django.db import models

# local import here.

# Abstract Classes


class TimeStampBase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ContactUs(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=80,
                            null=True,
                            blank=True,
                            help_text="Name")
    email = models.EmailField(max_length=80,
                              null=True,
                              blank=True,
                              help_text="Email")
    message = models.CharField(max_length=100,
                               null=True,
                               blank=True,
                               help_text="Message")

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
