from django.urls import URLPattern, URLResolver, path

from .views import film, home

urlpatterns = [
    path("", home, name="web"),
    path("api/", film, name="api"),
]
