from django.urls import path 
from . import views
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetCompleteView

from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path("",views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("password_reset/", PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="password_reset"),
    path("reset_password_sent/",PasswordResetDoneView.as_view(template_name="accounts/reset_password_sent.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(template_name="accounts/reset_confirm_form.html"), name="password_reset_confirm"),
    path("password_reset_complete/",PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name="password_reset_complete"),

    ## Image operations 

    path("upload/", views.upload_Image, name="upload_page"),
    path("details/<int:pk>/", views.details, name="detail"),
    path("delete/<int:pk>/", views.delete_image, name="delete")
    


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)