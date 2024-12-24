from django.contrib.auth import logout
from django.shortcuts import redirect

def check_user_approval(get_response):
    def middleware(request):
        if request.user.is_authenticated and not request.user.is_approved:
            logout(request)
            return redirect('approval_required')  # Inform user they need approval
        return get_response(request)
    return middleware