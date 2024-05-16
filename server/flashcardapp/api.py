from ninja import NinjaAPI, Schema

api = NinjaAPI()


class DesckSchema(Schema):
    name: str


@api.get("/deck", response=DesckSchema)
def deck(request):

    # query list of decks from database
    return
