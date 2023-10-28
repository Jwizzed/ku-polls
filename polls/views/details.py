"""A module for detail view."""
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from polls.models import Question, Choice, Vote


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
        except (Http404, OverflowError):
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
