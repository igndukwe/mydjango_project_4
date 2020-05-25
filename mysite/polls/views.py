# from django.http import Http404
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from django.template import loader

from .models import Question

# Create your views here.
# def index(request):
# @Anyi - ve in '-pub_date' is in the reverse order
# so that the latest publication dates show up first
# latest_question_list = Question.objects.order_by("-pub_date")[:5]
# for each question, give us its text
# and saperate each word by commas
# output = ", ".join([q.question_text for q in latest_question_list])
# return HttpResponse(output)


# def index(request):
# @Anyi: get top 5 questions
##latest_question_list = Question.objects.order_by("-pub_date")[:5]

# @Anyi: the path to the html template
##template = loader.get_template("polls/index.html")

# @Anyi: this context will be passed to the html template
##context = {
##    "latest_question_list": latest_question_list,
##}

# @Anyi: pass this context to the html template
##return HttpResponse(template.render(context, request))


def index(request):
    # @Anyi: get top 5 questions
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    return render(
        request, "polls/index.html", {"latest_question_list": latest_question_list}
    )


# def detail(request, question_id):
#   return HttpResponse("You're looking at question %s." % question_id)

##def detail(request, question_id):
##    try:
##       question = Question.objects.get(pk=question_id)
##    except Question.DoesNotExist:
##       raise Http404("Question does not exist")
##    return render(request, "polls/detail.html", {"question": question})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
