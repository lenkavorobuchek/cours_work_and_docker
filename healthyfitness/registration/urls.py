from django.contrib import auth
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterUser, LoginUser, logout_user

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('registration/', RegisterUser.as_view(), name='registration_field'),
    path('logout/', logout_user, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password-reset.html'),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password-reset_done.html'),
         name='password_reset_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password-change.html'),
         name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password-change_done.html'),
         name='password_change_done'),
    path('reset/<uidb64>/<token>//', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password-reset_form.html'),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password-reset_complete.html'),
         name='password_reset_complete'),

]