from django.contrib.auth.decorators import login_required
from django.core.handlers.asgi import HttpRequest, HttpResponse
from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from social_core.backends.github import GithubOAuth2

from .models import Film, Director
from rest_framework import generics
from .serializers import DirectorSerializer, FilmSerializer

from .decorators import *


class DirectorList(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    class DirectorDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Director.objects.all()
        serializer_class = DirectorSerializer

        def update(self, request, *args, **kwargs):
            partial = kwargs.pop('partial', False)
            instance = self.get_object()

            name = request.data.get('name', instance.name)

            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            return Response(serializer.data)


class FilmList(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        title = request.data.get('title', instance.title)
        year = request.data.get('year', instance.year)

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


@csrf_exempt
@require_http_methods(["GET"])
@api_auth_required("github")
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
@api_auth_required("github")
def get_all(request: HttpRequest) -> JsonResponse:
    films = Film.objects.all()
    data = [{"id": str(f.id), "title": f.title, "year": f.year} for f in films]
    return JsonResponse({"data": data})


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "Boom.html")


def login_view(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")
