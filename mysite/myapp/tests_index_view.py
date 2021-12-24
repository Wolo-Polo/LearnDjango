import datetime

from django.core import serializers
from django.test import TestCase
from .models import Question, Answer
from .views import IndexView
import json


# Create your tests here.
class IndexViewTest(TestCase):
    def setUp(self):
        number_of_question = 5
        date_create = datetime.datetime.now()
        for question_id in range(number_of_question):
            Question.objects.create(
                question='1',
                datetime_create=date_create
            )

    def test(self):
        # test url
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        # test correct template
        self.assertTemplateUsed(response, "myapp/index.html")

        # tes list question in view
        questions_expected = Question.objects.all()
        # print(serializers.serialize('json', questions_expected))
        questions_actual = response.context["questions"]
        # print(serializers.serialize('json', questions_actual))
        self.assertEqual(serializers.serialize('json', questions_expected), serializers.serialize('json', questions_actual))
