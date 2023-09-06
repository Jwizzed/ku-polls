import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question


def create_question(question_text, pub_days=None, end_days=None, pub_datetime=None, end_datetime=None):
    """
    Create a question with the given `question_text`.
    Optionally, you can provide either days offsets for publication and ending or exact datetimes.
    """
    if pub_days is not None:
        pub_time = timezone.now() + datetime.timedelta(days=pub_days)
    else:
        pub_time = pub_datetime

    if end_days is not None:
        end_time = timezone.now() + datetime.timedelta(days=end_days)
    else:
        end_time = end_datetime

    return Question.objects.create(question_text=question_text, pub_date=pub_time, end_date=end_time)


class CanVoteTest(TestCase):
    def test_can_vote_no_end_date(self):
        """A question without an end date and with a publication date in the past allows voting."""
        question = create_question("Past question without end date.", pub_days=-5)
        self.assertTrue(question.can_vote())

    def test_cannot_vote_no_end_date(self):
        """A question without an end date and with a publication date in the future does not allow voting."""
        question = create_question("Future question without end date.", pub_days=5)
        self.assertFalse(question.can_vote())


    def test_can_vote_with_end_date(self):
        """
        A question with a publication date in the past and an end date in the future allows voting.
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
        """A question does not allow voting right at the moment of its closing."""
        now = timezone.now()
        question = create_question("Question ended now.",
                                   pub_datetime=now - datetime.timedelta(
                                       days=1), end_datetime=now)
        self.assertFalse(question.can_vote())

    def test_future_question_with_future_end_date(self):
        """
        A question with both publication and end dates in the future does not allow voting.
        """
        question = create_question("Future question with future end date.",
                                   pub_days=5, end_days=10)
        self.assertFalse(question.can_vote())

    def test_past_question_with_past_end_date(self):
        """
        A question with both publication and end dates in the past does not allow voting.
        """
        question = create_question("Past question with past end date.",
                                   pub_days=-10, end_days=-5)
        self.assertFalse(question.can_vote())


class QuestionDetailViewTests(TestCase):
    """
    Test for QuestionDetailView
    """
    def test_future_question(self):
        """The detail view of a question with a pub_date in the future returns a 404 not found."""
        future_question = create_question("Future question.", pub_days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text='Past Question.',
                                        pub_days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)


class QuestionIndexViewTests(TestCase):
    """
    Test for QuestionIndexView
    """
    def test_no_questions(self):
        """If no questions exist, an appropriate message is displayed."""
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = create_question(question_text="Past question.", pub_days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", pub_days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question = create_question(question_text="Past question.", pub_days=-30)
        create_question(question_text="Future question.", pub_days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        question1 = create_question(question_text="Past question 1.", pub_days=-30)
        question2 = create_question(question_text="Past question 2.", pub_days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question2, question1],
        )


class ResultsViewTests(TestCase):
    """
    Test for ResultsView
    """
    def test_future_question_result(self):
        """If a question is not published yet, it should not show the result page."""
        question = create_question("Future", pub_days=3)
        url = reverse('polls:results', args=(question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_past_question_result(self):
        """The results view of a question with a pub_date in the past should display the results."""
        question = create_question("Past", pub_days=-3)
        url = reverse('polls:results', args=(question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_ongoing_question_result(self):
        """
        The results view for a question that's ongoing (published but not yet ended) should be accessible.
        """
        question = create_question("Ongoing", pub_days=-3, end_days=3)
        url = reverse('polls:results', args=(question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_ended_question_result(self):
        """
        The results view for a question that has already ended should be accessible.
        """
        question = create_question("Ended", pub_days=-10, end_days=-5)
        url = reverse('polls:results', args=(question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_not_started_question_result(self):
        """
        The results view for a question that has not started yet (both publication and end dates in the future) should not be accessible.
        """
        question = create_question("Not Started Yet", pub_days=5, end_days=10)
        url = reverse('polls:results', args=(question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
