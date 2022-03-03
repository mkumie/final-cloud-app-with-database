from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3



class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 3




class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date','total_enrollment')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']
    filter_horizontal = ('instructors',)



class QuestionAdmin(admin.ModelAdmin):
    list_display = ['course']
    inlines = [ChoiceInline]
    exclude = ('grade',)



class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question']




admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
