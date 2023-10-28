"""A module that represents the Vote model."""
from django.contrib.auth.models import User
from django.db import models


class Vote(models.Model):
    """Records a Vote of a Choice by a User."""

    choice = models.ForeignKey('Choice', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        """Meta class for Vote model."""
        db_table = "polls_vote"
        app_label = "polls"
