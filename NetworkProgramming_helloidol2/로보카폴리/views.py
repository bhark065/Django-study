from django.shortcuts import render
from django.views.generic import ListView, DetailView

from 로보카폴리.models import Character


# Create your views here.
class CharacterListView(ListView):
    model = Character
    # character_list = Character.objects.all() # DB에 모델 데이터 다 가져온다.

    # 모델_list.html에 모델_list라는 키로 DB에서 가져온 데이터 넣어서 render한다.
    # return render(request, '로보카폴리/character_list.html', context={'character_list: character_list'})

class CharacterListDetail(DetailView):
    model = Character
    # character = Character_objects.get(pk=pk)
    # return render(rquest, '로보카폴리/character_detail.html', context={'character: character'})
