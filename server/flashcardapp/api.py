from ninja import NinjaAPI, Schema
from flashcardapp.models import Deck

api = NinjaAPI()


class DesckSchema(Schema):
    name: str


@api.get("/deck")
def deck(request):

    # query list of all decks from database
    deck_list = Deck.objects.all().values()

    return {"decks": list(deck_list)}
