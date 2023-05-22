from django.urls import URLPattern, URLResolver, path, include

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

    path('social_auth/', include('social_django.urls', namespace='social')),
    path('logged/', login_view, name='login'),

]
