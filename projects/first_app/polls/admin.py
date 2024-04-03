from django.contrib import admin

from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    # Options for the 'list view' of questions
    ordering = ("id",)
    list_display = ("question_text", "id", "pub_date",)

    # Options for the 'detailed view' of questions
    fields = ["pub_date", "question_text"]


class ChoiceAdmin(admin.ModelAdmin):
    ordering = ("question", "choice_text",)
    list_display = ("choice_text", "question", "votes")


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
