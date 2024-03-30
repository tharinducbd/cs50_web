from django.contrib import admin

from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_display = ("id", "question_text", "pub_date",)

class ChoiceAdmin(admin.ModelAdmin):
    ordering = ("question", "choice_text",)
    list_display = ("choice_text", "question", "votes")


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
