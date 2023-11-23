from django.http import HttpResponse
from django.shortcuts import redirect

# Create a decorator for passes for certain user roles
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Sorry. You are not authorized to access this page.')
        return wrapper_func
    return decorator