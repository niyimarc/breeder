from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegForm, ContactForm, OfferForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Puppy, BlogPost
from django.views.generic import ListView, DetailView
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
            messages.success(request, "Account successfully created!")
            return redirect("home")
    else:
        regform = RegForm()
        messages.error(request, "Account not created!")
    return render(request, "app/signup.html") 

@login_required
def dashboard(request):
    puppy = Puppy.objects.filter(status="Available").order_by('-created_date')[:4]
    post = BlogPost.objects.filter(status=1).order_by('-created_date')[:2]
    current_user = request.user
    if request.method == "POST":
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contact = contactform.save(commit=False)
            contact.user = current_user
            contact.save()
            messages.success(request, "Message successfully submitted!")
            return HttpResponseRedirect('/dashboard')
        else:
            messages.error(request, "Message not submitted! Please fill out all fields correctly")
    else:
        contactform = ContactForm()
    return render(request, "app/dashboard.html", {'current_user': current_user, 'puppy': puppy, 'post': post,})

# def litters(request):
#     current_user = request.user
#     puppy = Puppy.objects.filter(status="Available").order_by('-created_date')[:4]
#     return render(request, "app/litters.html", {'current_user': current_user, 'puppy': puppy})

class ListPuppy(ListView):
    model = Puppy
    queryset = Puppy.objects.all().order_by('-created_date')
    template_name = 'app/litters.html'
    context_object_name = 'list_puppies'

def puppy_detail(request, slug):
    template_name = 'app/detail_puppy.html'
    puppy = get_object_or_404(Puppy, slug=slug)
    images = puppy.images.filter(active=True)
    new_image = None
    current_user = request.user
 
    if request.method == 'POST':
        offer_form = OfferForm(data=request.POST)
        if offer_form.is_valid():  
            new_offer = offer_form.save(commit=False)  
            new_offer.puppy = puppy
            new_offer.user = current_user
            new_offer.save()       
            messages.success(request, "Offer successfully submitted!")
            return HttpResponseRedirect('/puppy_detail/' + puppy.slug )
        else:
            messages.error(request, "Offer not submitted.")         
    else:
        offer_form = OfferForm()
    return render(request, template_name, {'puppy': puppy,
                                           'current_user': current_user,
                                           'offer_form': offer_form,
                                           'images': images,
                                           'new-image': new_image})

def post_detail(request, slug):
    template_name = 'app/detail_post.html'
    post = get_object_or_404(BlogPost, slug=slug)
    current_user = request.user
    return render(request, template_name, {'post': post,
                                           'current_user': current_user,})
    
class ListPost(ListView):
    model = BlogPost
    queryset = BlogPost.objects.all().order_by('-created_date')
    template_name = 'app/blog.html'
    context_object_name = 'list_posts'