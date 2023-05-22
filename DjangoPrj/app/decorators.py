from functools import wraps
from django.http import HttpResponseForbidden
from social_django.models import UserSocialAuth
from django.contrib.auth.models import AnonymousUser


def api_auth_required(provider):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            print(request.user.is_authenticated)
            authorization_header = request.headers.get('Authorization')
            if request.user.is_authenticated:
                return view_func(request, *args, **kwargs)

            return HttpResponseForbidden('Unauthorized')

        return wrapper

    return decorator
