from django.contrib import admin

# Register your models here.
from .models import Question, Choice

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Pollster Admin"

# admin.site.register(Question)
# admin.site.register(Choice)


class ChoiceInline(admin.TabularInline):
    model = Choice
    # how many extra fields
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'],
                                       'classes': ['collapse']}), ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
