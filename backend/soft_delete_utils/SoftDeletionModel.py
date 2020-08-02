from django.db import models
import datetime
import sys
import os
__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(__dir__, '..', '..'))
from soft_delete_utils import SoftDeletionManager  # noqa: E402


class SoftDeletionModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = datetime.datetime.now()
        self.save()

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()
