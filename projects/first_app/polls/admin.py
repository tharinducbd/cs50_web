from django.contrib import admin

from .models import Question, Choice


class ChoiceAdmin(admin.ModelAdmin):
    ordering = ("question", "choice_text",)
    list_display = ("choice_text", "question", "votes")


admin.site.register(Question)
admin.site.register(Choice, ChoiceAdmin)
