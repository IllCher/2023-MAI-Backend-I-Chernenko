from django.urls import URLPattern, URLResolver, path

from .views import *

urlpatterns = [
    path("", home, name="web"),
    path("api/search", search, name="search"),
    path("api//", get_all, name="getall"),
    path("api/create", add_film, name="create"),
    path("api/directors/", DirectorList.as_view(), name="director-list"),
    path("api/directors/<uuid:pk>/", DirectorDetail.as_view(), name="director-detail"),
    path("api/films/", FilmList.as_view(), name="film-list"),
    path("api/films/<uuid:pk>/", FilmDetail.as_view(), name="film-detail"),

]
