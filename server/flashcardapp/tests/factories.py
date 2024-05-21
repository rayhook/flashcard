import factory
from flashcardapp.models import DeckSchema


class DeckFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DeckSchema
        name = factory.Faker("word")
