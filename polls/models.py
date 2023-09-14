import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Question(models.Model):
    """
    A class response for Question model, also a table in database.

    :param models.Model: A class that represent a table in database.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published', auto_now_add=False)
    end_date = models.DateTimeField(
        "Date closed", default=None, null=True, blank=True
    )

    @property
    def total_votes(self):
        """
        Calculate the total votes for all choices related to this question.

        :return: Total votes count.
        """
        return Vote.objects.filter(choice__question=self).count()

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

    def is_published(self):
        """
        Check if the question is published.

        :return: True if the question is published, otherwise return False.
        """
        now = timezone.now()
        return now >= self.pub_date

    def can_vote(self):
        """
        Check if voting is allowed for the question.

        :return: True if the current time falls between the publication date
                 and the end date (if specified). Otherwise, return False.
        """
        now = timezone.now()
        if self.end_date is not None:
            return self.pub_date <= now <= self.end_date
        else:
            return self.pub_date <= now


class Choice(models.Model):
    """
    A class response for Choice model, also a table in database.

    :param models.Model: A class that represent a table in database.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
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


class Vote(models.Model):
    """Records a Vote of a Choice by a User."""
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
