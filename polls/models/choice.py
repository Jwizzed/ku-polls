"""A module that represents the Choice model."""
from django.db import models


class Choice(models.Model):
    """
    A class response for Choice model, also a table in database.

    :param models.Model: A class that represent a table in database.
    """

    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    @property
    def votes(self):
        """
        Count the votes for this choice.

        :return: The number of votes for this choice.
        """
        return self.vote_set.count()

    def __str__(self):
        """
        :return: The choice text
        """
        return self.choice_text

    class Meta:
        """Meta class for Choice model."""
        db_table = "polls_choice"
        app_label = "polls"
