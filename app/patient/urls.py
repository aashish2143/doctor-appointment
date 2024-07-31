from django.urls import path
from . import views

app_name = "patient"

urlpatterns = [
    path('login/', views.login_view, name='pa-login'),
    path('register/', views.register_view, name='pa-register'),
    path('forgot-password/', views.forgot_password_view, name='pa-forgot-pass'),
    path('password-change/', views.password_change_view, name='pa-pass-change'),
]
