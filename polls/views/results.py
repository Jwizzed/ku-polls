"""A module for results view."""
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.views import generic
from django.contrib import messages
from polls.models import Question


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
