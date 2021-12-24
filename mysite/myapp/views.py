import datetime

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Question, Answer


# Create your views here.
class IndexView(generic.ListView):
    template_name = "myapp/index.html"
    context_object_name = "questions"

    def get_queryset(self):
        question_all = Question.objects.all()
        try:
            limit = self.request.GET['limit']
        except KeyError:
            limit = 5
        paginator = Paginator(object_list=question_all, per_page=limit)
        try:
            page = self.request.GET['page']
            questions = paginator.page(page)
        except KeyError:
            questions = paginator.page(1)
        except PageNotAnInteger:
            questions = paginator.page(1)
        except EmptyPage:
            questions = paginator.page(1)
        return questions


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
    return HttpResponseRedirect(reverse("myapp:result", None, (question.id,)))


def create_question_view(request):
    if request.method == "GET":
        return render(request, "myapp/create.html", {})
    elif request.method == "POST":
        question_text = request.POST["question"]
        if question_text == "":
            return render(request, "myapp/create.html", {"status": "Fail"})
        question = Question(question=question_text, datetime_create=datetime.datetime.now())
        question.save()
        # idQuestion = question.id
        totalAnswer = 4
        for i in range(totalAnswer):
            answer_text = request.POST["answer" + str(i + 1)]
            if answer_text != "":
                answer = Answer(question=question, answer=answer_text, votes=0)
                answer.save()
        return render(request, "myapp/create.html", {"status": "Success"})
