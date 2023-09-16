from django.test import TestCase
from django.urls import reverse
from polls.tests.utils import create_question


class QuestionDetailViewTests(TestCase):
    """
    Test for QuestionDetailView
    """

    def test_future_question(self):
        """The detail view of a question with a pub_date in the future
        \returns a 302 redirect"""
        future_question = create_question("Future question.", pub_days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

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
