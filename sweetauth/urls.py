from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('user-signup/', views.signup, name = 'user-signup'),
    path('account-verify/', views.account_verify, name = 'account-verify'),
    path('user-login/', views.sweet_user_login, name = 'user-login'),
    path('user-logout/', views.user_logout, name = 'user-logout'),
    
    path("accounts/", include("django.contrib.auth.urls")),
    path('change-password/',auth_views.PasswordChangeView.as_view(
            template_name='registration/change-password.html',
            success_url = '/user-home'
        ),
        name='change_password'),
    path('password-reset/', auth_views.PasswordResetView.as_view
        (template_name = 'registration/password_reset_form.html'),
         name = 'password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name = 'registration/password_reset_done.html'
        ), name = 'password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name = 'registration/password_reset_complete.html'),
        name = 'password_reset_complete'),
]
