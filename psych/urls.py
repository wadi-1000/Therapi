from django.urls import path,include
from . import views

urlpatterns = [
    path('landing/', views.landing, name = 'landing'),
    path('home/',views.home, name = 'home'),
    path('add_article/',views.uploadArticle, name = 'add_article'),
    path('articles/', views.viewArticles, name = 'articles'),
    path('single_article/<int:pk>/',views.singleArticle, name = 'single_article'),
    path('make_appointment/',views.makeAppointment, name = 'make_appointment'),
    path('appointments/',views.myAppointments, name = 'appointments')
]