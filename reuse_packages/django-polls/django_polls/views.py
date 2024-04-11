from typing import Any
from django.db.models import F
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Choice, Question


# Works on IndexView(), but not used for now.
def check_choice_availability(question):
    if len(question.choice_set.all()) != 0:
        return True
    else:
        return False


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to
        be published in the future).
        """
        past_questions = Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")
        past_questions_with_choices = []
        for q in past_questions:
            if len(q.choice_set.all()) != 0:
                past_questions_with_choices.append(q)
        return past_questions_with_choices[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Exclude any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        """
        Exclude any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


# def results(request, question_id):
#     question = get_object_or_404(Question, id=question_id)
#     return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = question.choice_set.get(id=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))
