from django.contrib import admin

from app.cards.models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("id", "token", "count", "recipient")
    list_display_links = ("id", "token")
    search_fields = ["token", "content"]
    list_filter = ("recipient", "count")
