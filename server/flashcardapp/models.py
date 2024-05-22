from django.db import models


class Deck(models.Model):
    name = models.CharField(max_length=50)


class Card(models.Model):
    front = models.TextField()
    back = models.TextField()
    is_learned = models.BooleanField(default=False)
    deck = models.ForeignKey(
        "flashcardapp.Deck", related_name=("cards"), on_delete=models.CASCADE, null=True
    )
