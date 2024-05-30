from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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

class CharacterCreateView(CreateView):
    model = Character
    fields = ['name', 'feature', 'photo']                                # '__all__'
    template_name_suffix = '_create'                            # character_form.html -> character_create.html
    success_url = reverse_lazy('로보카폴리:character_list')      # 만들기 성공할 때 이동할 url

class CharacterUpdateView(UpdateView):
    model = Character
    fields = '__all__'                                      # ['name', 'feature', 'photo']
    template_name_suffix = '_update'                        # character_form.html -> character_update.html
    success_url = reverse_lazy('로보카폴리:character_list')  # 수정 성공할 때 이동할 url

class CharacterDeleteView(DeleteView):
    model = Character
    success_url = reverse_lazy('로보카폴리:character_list')  # 삭제 성공할 때 이동할 url