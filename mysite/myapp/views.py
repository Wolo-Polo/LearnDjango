from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F
from django.views import generic
from .models import Question, Answer


# Create your views here.
class IndexView(generic.ListView):
    template_name = "myapp/index.html"
    context_object_name = "questions"

    def get_queryset(self):
        # lấy danh sách question, order by datetime_create, lấy 5 phần tử đầu
        return Question.objects.order_by("-datetime_create")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "myapp/detail.html"


class ResultView(generic.DetailView):
    model = Question
    template_name = "myapp/result.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_answer = question.answer_set.get(pk=request.POST["vote"])
        # select_answer.votes += 1 # nếu sử dụng cách này 2 client vote cùng lúc có thể dẫn tới lỗi
        select_answer.votes = F("votes") + 1
        select_answer.save()
    except (KeyError, Answer.DoesNotExist):
        return render(request, "myapp/detail.html", {"error": "You didn't select a vote"})
    return HttpResponseRedirect(reverse("myapp:results", None, (question.id,)))
