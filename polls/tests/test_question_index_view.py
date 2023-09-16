from django.test import TestCase
from django.urls import reverse
from polls.tests.utils import create_question


class QuestionIndexViewTests(TestCase):
    """
    Test for QuestionIndexView
    """

    def test_future_question(self):
        """The detail view of a question with a pub_date in the future
        redirects to the index page"""
        future_question = create_question("Future question.", pub_days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = create_question(question_text="Past question.",
                                   pub_days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question = create_question(question_text="Past question.",
                                   pub_days=-30)
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
        question1 = create_question(question_text="Past question 1.",
                                    pub_days=-30)
        question2 = create_question(question_text="Past question 2.",
                                    pub_days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question2, question1],
        )
