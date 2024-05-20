from django.urls import path

from 로보카폴리 import views

app_name = '로보카폴리'

urlpatterns = [
    path('', views.CharacterListView.as_view(), name='character_list'),
]