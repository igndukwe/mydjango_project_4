from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from django.utils import timezone

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    # Anyi: this is the default context_object_name for ListViews
    # context_object_name = "question_list"
    # Anyi: override the default context_object_name
    # from "question_list" to "latest_question_list"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        # -pub_date prints articles will be in revered order so that recent articles appear first
        # return Question.objects.order_by("-pub_date")[:5]
        # pub_date__lte: publication date is less than or equals to
        return Question.objects.filter(pub_date__lte=timezone).order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    # Anyi: this is the default context_object_name for DetailView
    # context_object_name = "question"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    # Anyi: this is the default context_object_name for DetailView
    # context_object_name = "question"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {"question": question, "error_message": "You didn't select a choice.",},
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
