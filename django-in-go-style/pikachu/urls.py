from django.urls import path
from pikachu.views import PikachuViewSet

urlpatterns = [
    path("pikachu/", PikachuViewSet.as_view({"get": "list", "post": "create"}), name="pikachu-list"),
    path("pikachu/<uuid:pk>/", PikachuViewSet.as_view({"get": "retrieve", "put": "partial_update", "delete": "delete"}), name="pikachu-detail"),
]
