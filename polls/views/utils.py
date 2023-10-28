"""Utility functions for views."""
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from polls.models import Question, Choice, Vote
import logging


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
        logger.warning(f"{this_user} failed to vote for {question} from {ip}")
        return redirect("polls:index")

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        logger.warning(f"{this_user} failed to vote for {question}"
                       f" from {ip}")
        messages.error(request, "Please select a choice!")
        return redirect("polls:detail", pk=question_id)

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
