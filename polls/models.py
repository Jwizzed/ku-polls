import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    """
    A class response for Question model, also a table in database.

    :param models.Model: A class that represent a table in database.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """
        :return: The question text
        """
        return self.question_text

    def was_published_recently(self):
        """
        Checks if Question was published within the last day.

        :return: True if pub_date is within last day, False otherwise
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    """
    A class response for Choice model, also a table in database.

    :param models.Model: A class that represent a table in database.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """
        :return: The choice text
        """
        return self.choice_text
