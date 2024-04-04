from django.contrib import admin

from .models import Question, Choice


# 'Stacked In Line' view for Choice set in Question view
# class ChoiceInLine(admin.StackedInline):
#     model = Choice
#     extra = 3


# 'Tabular In Line' view for Choice set in Question view
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # Options for the 'list view' of questions
    ordering = ("id",)
    list_display = ("question_text", "id", "pub_date",)

    # Options for the 'detailed view' of questions
    # fields = ["pub_date", "question_text"]

    # Options for the 'detailed view' of questions: with 'field sets'
    fieldsets = [
        (None, {"fields": ["question_text",]}),
        ("Date information", {"fields": ["pub_date",], "classes": ["collapse",]}),
    ]
    inlines = [ChoiceInLine,]


class ChoiceAdmin(admin.ModelAdmin):
    ordering = ("question", "choice_text",)
    list_display = ("choice_text", "question", "votes")


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
