import datetime
from django.utils import timezone
from polls.models import Question


def create_question(question_text, pub_days=None, end_days=None,
                    pub_datetime=None, end_datetime=None):
    """
    Create a question with the given `question_text`.
    Optionally, you can provide either days offsets for publication and
    ending or exact datetimes.
    """
    if pub_days is not None:
        pub_time = timezone.now() + datetime.timedelta(days=pub_days)
    else:
        pub_time = pub_datetime

    if end_days is not None:
        end_time = timezone.now() + datetime.timedelta(days=end_days)
    else:
        end_time = end_datetime

    return Question.objects.create(question_text=question_text,
                                   pub_date=pub_time, end_date=end_time)
