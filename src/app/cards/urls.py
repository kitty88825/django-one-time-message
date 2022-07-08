from django.urls import path

from app.cards import views

urlpatterns = [
    # path('', views.show_card, name='show_card'),
    path("<str:token>/", views.show_card, name="show_card"),
]
