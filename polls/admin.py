from django.contrib import admin
from .models import Question,Choice


# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']
    inlines = [ChoiceInline]

    list_display = ['question','pub_date','was_published_recently']


admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)


