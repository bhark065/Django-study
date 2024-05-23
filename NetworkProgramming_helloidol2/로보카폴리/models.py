from django.db import models
from django.shortcuts import resolve_url


# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=20)                  # CharField()는 max_length 필수
    feature = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)    # 데이터 만들어질 때 자동으로 날짜, 시간 기록
    updated_at = models.DateTimeField(auto_now=True)        # 데이터 수정할 때 자동으로 날짜, 시간 기록

    def __str__(self): # 클래스를 출력할 때 이 함수를 호출하여 문자화한다.
        return f'이름: {self.name}, 특징: {self.feature}, 만든날짜: {self.created_at}, 수정한 날짜: {self.updated_at}'

    def get_absolute_url(self): # 이 객체 하나의 데이터를 가져오는 url
        return resolve_url('로보카폴리:detail', pk=self.id)