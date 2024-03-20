from django.contrib import admin

from .models import Quiz, Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3

class QuestionInline(admin.ModelAdmin):
    inlines = [AnswerInline]
admin.site.register(Question, QuestionInline)

class QuestionLinkInline(admin.TabularInline):
    # solution for nested inlines taken from
    # https://stackoverflow.com/questions/14308050/django-admin-nested-inline
    model = Question
    fields = ('text', 'question_type')
    extra = 1
    show_change_link = True

class QuizAdmin(admin.ModelAdmin):
    fields = ["title", "topics", "pub_date"]
    inlines = [QuestionLinkInline]

admin.site.register(Quiz, QuizAdmin)