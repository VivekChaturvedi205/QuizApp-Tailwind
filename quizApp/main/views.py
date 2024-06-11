from django.shortcuts import redirect, render,get_object_or_404
from . import forms
from .  import models
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from .forms import UsernamePasswordResetForm


def home(request):
    return render(request, 'home.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = forms.Registeruser(request.POST)
        if form.is_valid():
            form.save()
            msg = "Data saved successfully"
            form = forms.Registeruser()
    else:
        form = forms.Registeruser()
    return render(request, 'registration/register.html', {'form': form, 'msg': msg})

def all_categories(request):
    catData=models.QuizCategory.objects.all()
    return render(request, 'all_category.html',{'catData': catData})

@login_required
def category_question(request, cat_id):
    category = get_object_or_404(models.QuizCategory, id=cat_id)
    
    if not check_attempt_limit(request.user, category):
        return redirect('attempt-limit')
    questions = models.QuizQuestion.objects.filter(category=category).order_by('id').first()
    return render(request, 'category_question.html', {'catQuest': questions, 'category': category})

@login_required
def submit_answer(request,cat_id,question_id):
    if request.method=="POST":
        category=get_object_or_404(models.QuizCategory,id=cat_id)
        questions=models.QuizQuestion.objects.filter(category=category,id__gt=question_id).exclude(id=question_id).order_by('id').first()
        quest=get_object_or_404(models.QuizQuestion,id=question_id)
        user=request.user
        if 'skip' in request.POST:
            answer='Not Submitted'
        else:
            answer=request.POST['answer']
        models.submitanswer.objects.create(user=user,question=quest,right_answer=answer)
        check_attempt_limit(user, category)
        if questions:
            return render(request, 'category_question.html',{'catQuest': questions,'category':category})  
        else:
            result=models.submitanswer.objects.filter(user=user)  
            skipped = result.filter(right_answer='Not Submitted').count()
            attempted = result.exclude(right_answer='Not Submitted').count() 
            rightAns = sum(1 for row in result if row.question.right_opt == row.right_answer)
            percentage = (rightAns * 100) / result.count() if result.count() > 0 else 0

            return render(request, 'result.html', {
                'result': result,
                'skipped': skipped,
                'attempted': attempted,
                'rightAns': rightAns,
                'percentage': percentage
            })
    else:
        return render(request, 'method_not_allowed.html', status=405)     
    
def check_attempt_limit(user, category):
    hours_limit = 24
    count_attempt = models.UsercategoryAttempts.objects.filter(user=user, category=category).count()
    if count_attempt == 0:
        models.UsercategoryAttempts.objects.create(user=user, category=category)
        return True
    else:
        last_attempt = models.UsercategoryAttempts.objects.filter(user=user, category=category).order_by('-id').first()
        future_time = last_attempt.attempt_time + timedelta(hours=hours_limit)

        if timezone.now() < future_time:
            return False
        else:
            models.UsercategoryAttempts.objects.create(user=user, category=category)
            return True      
    
@login_required
def attempt_limit(request):
    return render(request, 'attempt_limit.html')


def forgot_password(request):
    if request.method == 'POST':
        form = UsernamePasswordResetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            new_password = form.cleaned_data.get('new_password1')

            try:
                user = User.objects.get(username=username)
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)  
                return redirect('password_reset_complete')
            except User.DoesNotExist:
                form.add_error('username', 'User does not exist.')

    else:
        form = UsernamePasswordResetForm()

    return render(request, 'forgot_password.html', {'form': form})

def password_reset_complete(request):
    return render(request, 'successfully.html')
