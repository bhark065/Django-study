from django.urls import path
from seventeen import views

app_name = "seventeen"

urlpatterns = [
    path('원우_html/', views.show_원우, name="원우"),
    path('디에잇_html/', views.show_디에잇, name="디에잇"),
]