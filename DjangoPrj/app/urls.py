from django.urls import URLPattern, URLResolver, path

from .views import *

urlpatterns = [
    path("", home, name="web"),
    path("api/search", search, name="search"),
    path("api//", get_all, name="getall"),
    path("api/create", add_film, name="create"),

]
