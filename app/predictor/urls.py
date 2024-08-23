from django.urls import path

from . import views

app_name = "predictor"

urlpatterns = [
    path('predict/', views.predict_disease, name='pre-disease'),
    path('book_doctor/', views.book_doctor, name='book_doctor'),

]