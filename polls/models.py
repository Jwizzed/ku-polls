import datetime
from django.db import models
from django.utils import timezone
from django.db.models import Sum


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
    is_able_to_vote = models.BooleanField(default=True)

    @property
    def able_to_vote(self):
        """
        Check if voting is allowed for the question.

        :return: True if the current time falls between the publication date
                 and the end date (if specified). Otherwise, return False.
        """
        if self.end_date:
            return self.is_published and timezone.now() <= self.end_date
        return self.is_published

    @property
    def total_votes(self):
        """
        Calculate the total votes for all choices related to this question.

        :return: Total votes count.
        """
        return self.choice_set.aggregate(Sum('votes'))['votes__sum'] or 0

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

    def save(self, *args, **kwargs):
        """
        Override the default save method to update the is_able_to_vote field
        based on the current value of the able_to_vote property before saving
        the instance to the database.

        :param args: Variable length argument list.
        :param kwargs: Arbitrary keyword arguments.
        """
        self.is_able_to_vote = self.able_to_vote
        super(Question, self).save(*args, **kwargs)


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
