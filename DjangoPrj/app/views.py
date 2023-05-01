from django.core.handlers.asgi import HttpRequest, HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Film, Director
from rest_framework import generics
from .serializers import DirectorSerializer, FilmSerializer


class DirectorList(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class FilmList(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


@csrf_exempt
@require_http_methods(["GET"])
def search(request: HttpRequest) -> JsonResponse:
    search_query = request.GET.get("query")
    films = Film.objects.filter(title__icontains=search_query)
    data = [{"id": str(f.id), "title": f.title, "year": f.year} for f in films]
    return JsonResponse({"data": data})


@csrf_exempt
@require_http_methods(["POST"])
def add_film(request: HttpRequest) -> JsonResponse:
    title = request.POST.get("title")
    year = request.POST.get("year")
    director_name = request.POST.get("director_name")

    director, created = Director.objects.get_or_create(name=director_name)

    film = Film.objects.create(title=title, year=year)
    film.directors.add(director)
    film.save()
    return JsonResponse({"id": str(film.id)})


@csrf_exempt
@require_http_methods(["GET"])
def get_all(request: HttpRequest) -> JsonResponse:
    films = Film.objects.all()
    data = [{"id": str(f.id), "title": f.title, "year": f.year} for f in films]
    return JsonResponse({"data": data})


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "Boom.html")
