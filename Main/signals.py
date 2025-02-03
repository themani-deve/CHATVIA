from django.shortcuts import redirect, reverse


def is_logged_in(views_func):
    def wrapper_func(request, *args, **kwargs):
        try:
            if request.user.is_authenticated:
                return views_func(request, *args, **kwargs)
            else:
                return redirect(reverse('login'))
        except Exception as e:
            print(f'Error is: {e}')

    return wrapper_func
