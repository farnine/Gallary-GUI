from django.urls import path 
from . import views
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetCompleteView
urlpatterns=[
    path("",views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("password_reset/", PasswordResetView.as_view(), name="password_reset"),
    path("reset_password_sent/",PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb 64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("password_reset_complete/",PasswordResetCompleteView.as_view(), name="password_reset_complete")
    


]