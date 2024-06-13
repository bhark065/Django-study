from django.urls import path

from chart_test import views

urlpatterns = [
    path('', views.show_chart, name='show_chart'),
]