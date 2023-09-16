"""This module contains polls app views."""
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Question, Choice, Vote
import logging


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
        return Question.objects.filter(pub_date__lte=timezone.now())\
            .order_by('-pub_date')


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

        try:
            user_vote = self.object.choice_set.filter(
                vote__user=request.user).last()
        except TypeError:
            user_vote = None

        context = self.get_context_data(object=self.object,
                                        user_vote=user_vote)

        if not self.object.can_vote():
            messages.error(request,
                           f"Poll {self.object} has ended and is not "
                           f"available for voting.")
            return redirect("polls:index")

        return self.render_to_response(context)


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
            max_votes = 30
            context = {
                "question": self.object,
                "max_votes": max_votes,
            }
            return render(request, self.template_name, context)


@login_required
def vote(request, question_id):
    """Process a vote on the detail view.

    :param request: Django request object
    :param question_id: ID of the question being voted on
    :return: Redirects to results page or detail page with error message
    """
    question = get_object_or_404(Question, pk=question_id)
    ip = get_client_ip(request)
    this_user = request.user
    logger = logging.getLogger("polls")
    logger.info(f"{this_user} logged in from {ip}")

    if not question.can_vote():
        messages.error(request, f"Poll number {question.id} "
                                f"is not available to vote")
        logger.warning(f"{this_user} failed to vote for {question}"
                          f" from {ip}")
        return redirect("polls:index")

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        logger.warning(f"{this_user} failed to vote for {question}"
                       f" from {ip}")
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "Please select a choice!",
        })

    try:
        curr_vote = Vote.objects.get(user=this_user, choice__question=question)
        curr_vote.choice = selected_choice
    except Vote.DoesNotExist:
        curr_vote = Vote(user=this_user, choice=selected_choice)
    curr_vote.save()

    logger.info(f"{this_user} voted for {question} from {ip}")
    messages.success(request, f"Your vote for {question} has been recorded.")
    return HttpResponseRedirect(reverse("polls:results",
                                        args=(question.id,)))


def get_client_ip(request):
    """Get the visitor’s IP address using request headers."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
