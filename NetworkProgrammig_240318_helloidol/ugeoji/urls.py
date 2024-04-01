from django.urls import path
from ugeoji import views

app_name = "ugeoji"

urlpatterns = [
    # path('seoyoung_html/', views.show_seoyoung, name="seoyoung"),
    # path('haewon_html/', views.show_haewon, name="haewon"),
    # path('seohyeon_html/', views.show_seohyeon, name="seohyeon")
    path('<멤버>/', views.show_멤버, name='멤버')
]