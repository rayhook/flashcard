from ninja import NinjaAPI, Schema
from typing import List
from flashcardapp.models import Deck, Card
from django.shortcuts import get_object_or_404
from django.db.models import Q

api = NinjaAPI()


# Schemas
class DeckSchema(Schema):
    name: str


class DeckIdSchema(Schema):
    deck_id: int


class CardSchemaIn(Schema):
    front: str
    back: str
    is_learned: bool
    deck_id: int


class CardSchemaOut(Schema):
    front: str
    back: str
    is_learned: bool


class CardUpdateSchedma(Schema):
    front: str = None
    back: str = None
    is_learned: bool = None


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


@api.delete("/deck/{int:deck_id}", response={204: None})
def delete_deck(request, deck_id: int):
    deck = get_object_or_404(Deck, pk=deck_id)
    deck.delete()
    return 204, None


@api.post("/card", response={201: None})
def create_card(request, payload: CardSchemaIn):
    deckInstance = get_object_or_404(Deck, pk=payload.deck_id)
    card = Card.objects.create(
        front=payload.front,
        back=payload.back,
        is_learned=payload.is_learned,
        deck=deckInstance,
    )
    return 201, None


@api.get("/card/{int:card_id}", response={200: CardSchemaOut})
def get_card(request, card_id: int):
    card = get_object_or_404(Card, pk=card_id)
    return 200, card


@api.delete("/card/{int:card_id}", response={204: None})
def delete_card(request, card_id: int):
    card = get_object_or_404(Card, pk=card_id)
    card.delete()
    return 204, None


@api.put("/card/update/{int:card_id}", response={200: CardSchemaOut})
def update_card(request, card_id: int, payload: CardUpdateSchedma):
    card = get_object_or_404(Card, pk=card_id)

    if payload.front is not None:
        card.front = payload.front
    if payload.back is not None:
        card.back = payload.back
    if payload.is_learned is not None:
        card.is_learned = payload.is_learned
    card.save()
    return 200, card
