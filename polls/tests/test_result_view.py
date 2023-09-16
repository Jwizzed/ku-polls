from django.test import TestCase
from django.urls import reverse
from polls.tests.utils import create_question


class ResultsViewTests(TestCase):
    """
    Test for ResultsView
    """

    def test_future_question_result(self):
        """If a question is not published yet, it should redirect to
        the index page"""
        question = create_question("Future", pub_days=3)
        url = reverse('polls:results', args=(question.id,))
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_past_question_result(self):
        """The results view of a question with a pub_date in the past
        should display the results."""
        question = create_question("Past", pub_days=-3)
        url = reverse('polls:results', args=(question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_ongoing_question_result(self):
        """
        The results view for a question that's ongoing (published but
        not yet ended) should be accessible.
        """
        question = create_question("Ongoing", pub_days=-3, end_days=3)
        url = reverse('polls:results', args=(question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_ended_question_result(self):
        """
        The results view for a question that has already ended should
        be accessible.
        """
        question = create_question("Ended", pub_days=-10, end_days=-5)
        url = reverse('polls:results', args=(question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_not_started_question_result(self):
        """
        The results view for a question that has not started yet
        (both publication and end dates in the future) should redirect
        to the index page.
        """
        question = create_question("Not Started Yet", pub_days=5, end_days=10)
        url = reverse('polls:results', args=(question.id,))
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
