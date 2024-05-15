from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/deck")
def deck(request):
    return "flashcard homepage"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
