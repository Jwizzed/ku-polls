"""This module contains polls app views."""
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from .models import Question, Choice
from django.contrib.auth.decorators import login_required


class IndexView(generic.ListView):
    """View to display the most recent 5 questions.

    :return: Rendered template with the latest 5 questions
    """
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Get the last 5 published questions excluding those in the future.

        :return: Queryset of the latest 5 questions
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    """View for displaying each question's detail.

    :param pk: Primary key of the question
    :return: Rendered template with question details
    """
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """Get questions that are already published.

        :return: Queryset of published questions
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    def get(self, request, *args, **kwargs):
        """Get the question object and render the template.

        :param request: Django request object
        :param args: Arguments
        :param kwargs: Keyword arguments
        :return: Rendered template with question details
        """
        question = super().get_object()

        if not question.can_vote():
            messages.error(request, f"Poll number {question.id} is not available to vote")
            return redirect("polls:index")

        return render(request, self.template_name, {"question": question})


class ResultsView(generic.DetailView):
    """View to display each question's result.

    :param pk: Primary key of the question
    :return: Rendered template with question's results
    """
    model = Question
    template_name = "polls/results.html"

    def get(self, request, *args, **kwargs):
        """Get the question object and render the template.

        :param request: Django request object
        :param args: Arguments
        :param kwargs: Keyword arguments
        :return: Rendered template with question's results
        """
        question = super().get_object()
        if not question.is_published():
            messages.error(request, f"Poll number {question.id} results are not available.")
            return redirect("polls:index")
        return render(request, self.template_name, {"question": question})


@login_required
def vote(request, question_id):
    """Process a vote on the detail view.

    :param request: Django request object
    :param question_id: ID of the question being voted on
    :return: Redirects to results page or detail page with error message
    """
    question = get_object_or_404(Question, pk=question_id)

    if not question.can_vote():
        messages.error(request, f"Poll number {question.id} is not available to vote")
        return redirect("polls:index")

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "Please select a choice!",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
