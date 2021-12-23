from django.contrib import admin
from .models import Question
from .models import Answer


# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question"]}),
        ("Đây là trường được chỉnh sửa cách hiển thị bằng ModelAdmin", {"fields": ["datetime_create"]})
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
