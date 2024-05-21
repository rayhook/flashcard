from ninja import NinjaAPI, Schema
from typing import List
from flashcardapp.models import Deck
from django.shortcuts import get_object_or_404

api = NinjaAPI()


class DeckSchema(Schema):
    name: str


@api.get("/deck", response={200: List[DeckSchema]})
def list_decks(request):

    decks = Deck.objects.all()

    return 200, decks


@api.get("/deck/{int:deck_id}", response={200: DeckSchema})
def get_deck(request, deck_id: int):
    deck = get_object_or_404(Deck, pk=deck_id)
    return 200, deck


@api.post("/deck", response={201: DeckSchema})
def create_deck(request, payload: DeckSchema):
    deck = Deck.objects.create(**payload.dict())
    return 201, deck
