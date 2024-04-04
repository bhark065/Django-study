from django.urls import path
from ugeoji import views

app_name = "ugeoji"

urlpatterns = [
    path('멤버리스트/', views.show_멤버리스트, name='멤버리스트'),
    path('<멤버>/', views.show_멤버, name='멤버'),
    # path('seoyoung_html/', views.show_seoyoung, name="seoyoung"),
    # path('haewon_html/', views.show_haewon, name="haewon"),
    # path('seohyeon_html/', views.show_seohyeon, name="seohyeon")
]