from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegForm, ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
# from .models import User
# Create your views here.

def login_excluded(redirect_to):
    """ This decorator kicks authenticated users out of a view """ 
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to) 
            return view_method(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper

# Create your views here.
@login_excluded('login')
def signup(request):
    if request.method == "POST":
        regform = RegForm(request.POST)
        if regform.is_valid():
            regform.save(commit=True)
            return redirect("home")
    else:
        regform = RegForm()
    return render(request, "app/signup.html") 

@login_required
def dashboard(request):
    current_user = request.user
    if request.method == "POST":
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contact = contactform.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.success(request, "Message successfully submitted!")
            return HttpResponseRedirect('/dashboard')
        else:
            messages.error(request, "Message not submitted! Please fill out all fields correctly")
    else:
        contactform = ContactForm()
    return render(request, "app/dashboard.html", {'current_user': current_user,})