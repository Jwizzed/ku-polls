from django.test import TestCase
from django.utils import timezone
import datetime
from polls.tests.utils import create_question


class CanVoteTest(TestCase):
    def test_can_vote_no_end_date(self):
        """A question without an end date and with a publication date in the
        past allows voting."""
        question = create_question("Past question without end date.",
                                   pub_days=-5)
        self.assertTrue(question.can_vote())

    def test_cannot_vote_no_end_date(self):
        """A question without an end date and with a publication date in the
         future does not allow voting."""
        question = create_question("Future question without end date.",
                                   pub_days=5)
        self.assertFalse(question.can_vote())

    def test_can_vote_with_end_date(self):
        """
        A question with a publication date in the past and an end date in
        the future allows voting.
        """
        question = create_question("Question with end date.", pub_days=-5,
                                   end_days=5)
        self.assertTrue(question.can_vote())

    def test_cannot_vote_after_end_date(self):
        """
        A question does not allow voting after its end date.
        """
        question = create_question("Question with past end date.",
                                   pub_days=-10, end_days=-5)
        self.assertFalse(question.can_vote())

    def test_can_vote_right_after_publishing(self):
        """A question allows voting right at the moment of its publication."""
        now = timezone.now()
        question = create_question("Question starts now.", pub_datetime=now)
        self.assertTrue(question.can_vote())

    def test_cannot_vote_right_after_closing(self):
        """A question does not allow voting right at the moment of
        its closing."""
        now = timezone.now()
        question = create_question("Question ended now.",
                                   pub_datetime=now - datetime.timedelta(
                                       days=1), end_datetime=now)
        self.assertFalse(question.can_vote())

    def test_future_question_with_future_end_date(self):
        """
        A question with both publication and end dates in the future does
        not allow voting.
        """
        question = create_question("Future question with future end date.",
                                   pub_days=5, end_days=10)
        self.assertFalse(question.can_vote())

    def test_past_question_with_past_end_date(self):
        """
        A question with both publication and end dates in the past does
        not allow voting.
        """
        question = create_question("Past question with past end date.",
                                   pub_days=-10, end_days=-5)
        self.assertFalse(question.can_vote())
