from django.contrib import admin
from .models import QuizCategory,QuizQuestion,submitanswer,UsercategoryAttempts

@admin.register(QuizCategory)
class QuizCategoryAdmin(admin.ModelAdmin):
    list_display=('title','detail')

@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display=('category','question','level')

@admin.register(submitanswer)
class submitanswerAdmin(admin.ModelAdmin):
    list_display=('question','question','right_answer')
    
@admin.register(UsercategoryAttempts)
class UsercategoryAttemptsAdmin(admin.ModelAdmin):
    list_display=('category','user','attempt_time')