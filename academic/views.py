from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
@login_required
def home_view(request):
    return render(request, "home.html")

def contact_form(request):
    return render(request,"contact_form.html")
    

def contact(request):
    if request.method =="POST":
        subject = request.POST["subject"]
        message = request.POST["message"] + "/Email: " + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER 
        email_to = ["aldomm61@gmail.com"]
        send_mail(subject, message, email_from, email_to, fail_silently = False)

        return render(request, "successful_contact.html")
    
    return render(request,"contact_form.html")



