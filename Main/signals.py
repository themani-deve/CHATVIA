from django.shortcuts import redirect, reverse
from functools import wraps


def is_logged_in(view_func):
    @wraps(view_func)
    def wrapper_func(request, *args, **kwargs):
        try:
            if request.user.is_authenticated:
                return view_func(request, *args, **kwargs)
            else:
                return redirect(reverse('login'))
        except Exception as e:
            print(f'Error is: {e}')
            return redirect(reverse('login'))

    return wrapper_func
