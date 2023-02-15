from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegForm, ContactForm, OfferForm, AppointmentForm, NewsletterForm, AnonymousContactForm, ProfileForm, ApplyForm
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
            return redirect("login")
    else:
        regform = RegForm()
        messages.error(request, "Account not created!")
    return render(request, "app/signup.html") 

def home(request):
    puppy = Puppy.objects.filter(status="Available").order_by('-created_date')[:6]
    post = BlogPost.objects.filter(status=1).order_by('-created_date')[:2]
    current_user = request.user
    if request.method == "POST":
        appointmentform = AppointmentForm(request.POST)
        if appointmentform.is_valid():
            appointment = appointmentform.save(commit=False)
            appointment.user = current_user
            appointment.save()
            messages.success(request, "Appointment successfully submitted!")
            return HttpResponseRedirect('/home')
        else:
            messages.error(request, "Appointment not submitted! Please fill out all fields correctly")
    else:
        contactform = AppointmentForm()

    # newsletter form 
    if request.method == "POST":
        newsletterform = NewsletterForm(request.POST)
        if newsletterform.is_valid():
            newsletterform.save()
            messages.success(request, "Email successfully added to our newsletter!")
            return HttpResponseRedirect('/home')
        else:
            messages.error(request, "Email not submitted! Please fill out all fields correctly")
    else:
        contactform = NewsletterForm()
    return render(request, "app/main/home.html", {'current_user': current_user, 'puppy': puppy, 'post': post,})

def contact(request):
    current_user = request.user

    # Anonymous user contact form 
    if request.method == "POST":
        anonymouscontactform = AnonymousContactForm(request.POST)
        if anonymouscontactform.is_valid():
            anonymouscontactform.save()
            messages.success(request, "Appointment successfully submitted!")
            
            return HttpResponseRedirect('/contact')
        else:
            messages.error(request, "Appointment not submitted! Please fill out all fields correctly")
    else:
        contactform = AnonymousContactForm()

    # newsletter form 
    if request.method == "POST":
        newsletterform = NewsletterForm(request.POST)
        if newsletterform.is_valid():
            newsletterform.save()
            messages.success(request, "Email successfully added to our newsletter!")
            return HttpResponseRedirect('/contact')
        else:
            messages.error(request, "Email not submitted! Please fill out all fields correctly")
    else:
        contactform = NewsletterForm()
    return render(request, "app/main/contact.html", {'current_user': current_user,})

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

    if request.method == "POST":
        profileform = ProfileForm(request.POST, instance=request.user.profile)
        if profileform.is_valid():
            profileform.save()
            messages.success(request, "Profile Edited Successfully!")
            return HttpResponseRedirect('/dashboard')
        else:
            messages.error(request, "Profile not edited!")
    else:
        profileform = ProfileForm(instance=request.user.profile)
    return render(request, "app/dashboard.html", {'current_user': current_user, 'puppy': puppy, 'post': post,})

class ListPuppy(ListView):
    model = Puppy
    queryset = Puppy.objects.all().order_by('-created_date')
    template_name = 'app/litters.html'
    context_object_name = 'list_puppies'

@login_required
def puppy_detail(request, slug):
    template_name = 'app/detail_puppy.html'
    puppy = get_object_or_404(Puppy, slug=slug)
    images = puppy.images.filter(active=True)
    new_image = None
    current_user = request.user
 
#  submit the OfferForm 
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

# submit the ApplyForm 
    if request.method == 'POST':
        apply_form = ApplyForm(data=request.POST)
        if apply_form.is_valid():  
            new_apply = apply_form.save(commit=False)  
            new_apply.puppy = puppy
            new_apply.user = current_user
            new_apply.save()       
            messages.success(request, "Application successfully submitted!")
            return HttpResponseRedirect('/puppy_detail/' + puppy.slug )
        else:
            messages.error(request, "Application not submitted.")         
    else:
        apply_form = ApplyForm()
    return render(request, template_name, {'puppy': puppy,
                                           'current_user': current_user,
                                           'offer_form': offer_form,
                                           'apply_form': apply_form,
                                           'images': images,
                                           'new-image': new_image})

def post_detail(request, slug):
    template_name = 'app/detail_post.html'
    post = get_object_or_404(BlogPost, slug=slug)
    images = post.images.filter(active=True)
    new_image = None
    current_user = request.user
    return render(request, template_name, {'post': post,
                                           'current_user': current_user,
                                           'images': images,
                                           'new-image': new_image})
    
class ListPost(ListView):
    model = BlogPost
    template_name = 'app/main/blog.html'
    context_object_name = 'list_posts'

    def get_context_data(self, **kwargs):
        context = super(ListPost, self).get_context_data(**kwargs)
        context.update({
            'puppy_list': Puppy.objects.filter(status="Available").order_by('-created_date')[:4],
            # 'more_context': Model.objects.all(),
        })
        return context

    def get_queryset(self):
        return BlogPost.objects.all().order_by('-created_date')

