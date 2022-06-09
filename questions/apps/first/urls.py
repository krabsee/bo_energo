from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('quadratic_equation/', views.QuadraticEquation.as_view()),
    path('color/', views.Color.as_view()),

]
