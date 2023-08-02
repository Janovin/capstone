# Customising @login_required decorator so that non logged in users are redirected
from django.shortcuts import redirect

def custom_login_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('user_auth:register')  # Redirect to the 'register' page
        return view_func(request, *args, **kwargs)
    return _wrapped_view
