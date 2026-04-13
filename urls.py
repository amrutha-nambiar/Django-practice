from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_home),
    path('details/', views.student_details),
]