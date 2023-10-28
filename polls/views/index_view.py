"""A module for index view."""
from django.views import generic
from django.utils import timezone
from polls.models import Question


class IndexView(generic.ListView):
    """A class for index view."""

    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now())\
            .order_by('-pub_date')
