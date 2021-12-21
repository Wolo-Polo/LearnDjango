from django.http import HttpResponse
from .models import Question
from django.template import loader


# Create your views here.
def index(request):
    response = HttpResponse()
    list_questions = Question.objects.order_by("-datetime_create")[:5] #lấy danh sách question, order by datetime_create, lấy 5 phần tử đầu
    print(list_questions)
    template = loader.get_template("myapp/index.html")
    context = {
        "questions": list_questions
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("Question: " + str(question_id))


def results(request, question_id):
    return HttpResponse("Answer " + str(question_id))


def vote(request, question_id):
    return HttpResponse("Vote " + str(question_id))

