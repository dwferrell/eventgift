from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import User

@login_required
def profile(request):
    user = User.objects.get(pk=request.user.pk)
    return render(request, 'profile.html', {'user': user})
