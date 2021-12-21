from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F
from .models import Question, Answer


# Create your views here.
def index(request):
    list_questions = Question.objects.order_by("-datetime_create")[:5]
    # lấy danh sách question, order by datetime_create, lấy 5 phần tử đầu

    context = {
        "questions": list_questions
    }
    return render(request, "myapp/index.html", context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "myapp/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "myapp/result.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_answer = question.answer_set.get(pk=request.POST["vote"])
        #select_answer.votes += 1 # nếu sử dụng cách này 2 client vote cùng lúc có thể dẫn tới lỗi
        select_answer.votes = F("votes") + 1
        select_answer.save()
    except (KeyError, Answer.DoesNotExist):
        return render(request, "myapp/detail.html", {"error": "You didn't select a vote"})
    return HttpResponseRedirect(reverse("myapp:results", None, (question.id,)))

