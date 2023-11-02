from django.contrib import admin

from .models import Choice, Question, Users


# Register your models here.
admin.site.site_header = 'Examen de Estres'


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


class UsersList(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name"]}),
        ("Data login", {"fields": ["data"]}),
    ]
    list_display = ["name", "data", "abort", "question_ID"]
    list_filter = ["data", "abort", "question_ID"]
    search_fields = ["name"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Users, UsersList)
