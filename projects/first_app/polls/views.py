from django.http import HttpResponse
from django.shortcuts import render

from .models import Question

def index(request):
    latest_question_obj_list = Question.objects.order_by("-pub_date")[:5]

    question_text_list = [q.question_text for q in latest_question_obj_list]
    output = ", ".join(question_text_list)

    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    response = f"Your're lookin at the results of question {question_id}"
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
