from django.core.handlers.asgi import HttpRequest, HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def film(request: HttpRequest) -> JsonResponse:
    if request.method == "GET":
        return JsonResponse({"title": "Title"}, status=200)
    elif request.method == "POST":
        return JsonResponse({"id": "33"}, status=201)
    return JsonResponse({"error": "invalid request"}, status=400)


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "Boom.html")
