from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('accounts/register', views.register, name="register"),
    path('all-categories', views.all_categories, name="allcategories"),
    path('categories/<int:cat_id>/', views.category_question, name="category_question"),
    path('submit-answer/<int:cat_id>/<int:question_id>', views.submit_answer, name='submit_answer'),
    path('attempt-limit', views.attempt_limit, name='attempt-limit'),
    path('forgot_password/',views.forgot_password, name='forgot_password'),
    path('password_reset_complete/', views.password_reset_complete, name='password_reset_complete'),
]
