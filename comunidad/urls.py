from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import *


urlpatterns = [
    path('comunidad', comunidad, name='comunidad'),

    path('peopleRegister', peopleRegister, name='peopleRegister'),
    path('profile/<int:pk>', profile, name='profile'),
    path('loginPage', loginPage, name='loginPage'),

    path('userLogout', userLogout, name='userLogout'),
    # path('editProfile', editProfile, name='editProfile'),

    path('comunity', comunity, name='comunity'),
    path('comunityRegister', comunityRegister, name='comunityRegister'),

    path('company', company, name='company'),
    path('companyRegister', companyRegister, name='companyRegister'),

    path('password/reset_password/',
        auth_views.PasswordResetView.as_view(template_name='comunidad/people/password/password_reset.html'),
        name='reset_password' ),
    path('password/reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name='comunidad/people/password/password_reset_sent.html'),
        name='password_reset_done'),
    path('password/reset/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(template_name='comunidad/people/password/password_reset_form.html'),
        name='password_reset_confirm'),
    path('password/reset_password_complete',
        auth_views.PasswordResetCompleteView.as_view(template_name='comunidad/people/password/password_reset_done.html'),
        name='password_reset_complete'),

]