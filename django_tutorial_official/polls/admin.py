from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),  # pylint: disable=C0326
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
