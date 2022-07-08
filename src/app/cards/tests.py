from django.test import TestCase


class ShowCardTest(TestCase):
    def test_uses_card_template(self):
        response = self.client.get("/cards/")
        self.assertTemplateUsed(response, "card.html")
