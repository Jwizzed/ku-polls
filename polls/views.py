"""This module contains polls app views."""
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from .models import Question, Choice
from django.contrib.auth.decorators import login_required
from django.db.models import Max


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
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')


class DetailView(generic.DetailView):
    """View for displaying each question's detail.

    :param pk: Primary key of the question
    :return: Rendered template with question details
    """
    model = Question
    template_name = "polls/detail.html"
    object: Question

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
        try:
            self.object = get_object_or_404(Question, pk=kwargs["pk"])
        except Http404:
            messages.error(request,
                           f"Poll with ID {kwargs['pk']} does not exist.")
            return redirect("polls:index")

        context = self.get_context_data(object=self.object)

        if not self.object.can_vote():
            messages.error(request,
                           f"Poll {self.object} has ended and is not available for voting.")
            return redirect("polls:index")

        return self.render_to_response(context)

#
# class ResultsView(generic.DetailView):
#     """View to display each question's result.
#
#     :param pk: Primary key of the question
#     :return: Rendered template with question's results
#     """
#     model = Question
#     template_name = "polls/results.html"
#     object: Question
#
#     def get(self, request, *args, **kwargs):
#         """Get the question object and render the template.
#
#         :param request: Django request object
#         :param args: Arguments
#         :param kwargs: Keyword arguments
#         :return: Rendered template with question's results
#         """
#         try:
#             self.object = get_object_or_404(Question, pk=kwargs["pk"])
#         except Http404:
#             messages.error(request,
#                            f"Poll number {kwargs['pk']} does not exists.")
#             return redirect("polls:index")
#
#         if not self.object.is_published():
#             messages.error(request,
#                            f"Poll {self.object} results are not "
#                            f"available.")
#             return redirect("polls:index")
#         else:
#             return render(request, self.template_name, {"question": self.object})


class ResultsView(generic.DetailView):
    """View to display each question's result.

    :param pk: Primary key of the question
    :return: Rendered template with question's results
    """
    model = Question
    template_name = "polls/results.html"
    object: Question

    def get(self, request, *args, **kwargs):
        """Get the question object and render the template.

        :param request: Django request object
        :param args: Arguments
        :param kwargs: Keyword arguments
        :return: Rendered template with question's results
        """
        try:
            self.object = get_object_or_404(Question, pk=kwargs["pk"])
        except Http404:
            messages.error(request,
                           f"Poll number {kwargs['pk']} does not exists.")
            return redirect("polls:index")

        if not self.object.is_published():
            messages.error(request,
                           f"Poll {self.object} results are not "
                           f"available.")
            return redirect("polls:index")
        else:
            max_votes = self.object.choice_set.aggregate(max_votes=Max('votes'))['max_votes'] or 0
            context = {
                "question": self.object,
                "max_votes": max_votes,
            }
            return render(request, self.template_name, context)


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
