"""Users views"""

#   Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

#   Models
from django.contrib.auth.models import User 
from users.models import Profile

#   Exceptions
from django.db.utils import IntegrityError

#    --------------login-----------------
def login_view(request):
    """Login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        # Redirect to a success page.
        else:
             return render(request, 'login.html',{'error': 'Invalid username or password'})
    return render(request, 'login.html')


#    --------------signup-----------------
def signup_view(request):
    """Sign up view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        #   creamos el usuario        
        if password != password_confirmation:
            return render(request, 'users/teachers/signup.html')
        
        #   Creamos un objeto para almacenar su informacion adicional
        try:
            user = User.objects.create_user(username = username, password = password)
        except IntegrityError:
            return render(request, 'users/teachers/signup.html')

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        #   Creamos el perfil del usuario
        profile = Profile(user = user)
        profile.save()

        #   Redirección al login 
        return redirect('login')

    return render(request, 'users/teachers/signup.html')


#    --------------logout-----------------
@login_required
def logout_view(request):
    """logout request"""
    logout(request)
    return redirect('login')




