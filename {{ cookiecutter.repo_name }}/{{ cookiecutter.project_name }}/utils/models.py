from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    """
    TimeStampedModel is the base abstract class to be used for all models with
    this project.
    """

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.pk}"
