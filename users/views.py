"""User views"""
#   Django
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


def login_view(request):
    """Login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,
                            username = username,
                            password = password
                        )
        
        if user:
            login(request, user)
            return redirect('home')
        
        else:
             return render(request, 'login.html',{'error': 'Invalid username or password'})
    return render(request, 'login.html')


