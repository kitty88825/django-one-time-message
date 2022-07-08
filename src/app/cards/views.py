from django.shortcuts import render

from app.cards.models import Card


def show_card(request, token):
    card_ = Card.objects.get(token=token)
    return render(request, "card.html", {"card": card_})
