
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView,LogoutView
from .models import User
from .forms import ServiceProviderForm,ServiceFinderForm
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import HttpResponse
from .models import Services

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def listing(request):
    return render(request, 'users/listing.html')

def category(request):
    return render(request, 'users/category.html')

def contact(request):
    return render(request, 'users/contact.html')

def about(request):
    return render(request, 'users/about.html')

def reviews(request):
    return render(request, 'users/reviews.html')


class SProviderSignUpView(CreateView):
    model = User
    form_class = ServiceProviderForm
    template_name = 'registration/sprovider_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type']= 'serviceprovider'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #//-->session
        login(self.request, user)
        return redirect('/')

class SFinderSignUpView(CreateView):
    model = User
    form_class = ServiceProviderForm
    template_name = 'registration/sfinder_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type']= 'servicefinder'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #//-->session
        login(self.request, user)
        return redirect('/')

class LoginView(LoginView):
    template_name = 'registration/login.html'

    def get(self, request, *args, ** kwargs):
        print(self.request.user)
        return self.render_to_response(self.get_context_data())  

class LogoutView(LogoutView):
    pass


# Create your views here.

def sendmail(request):
   subject = 'welcome'
   message = 'hello world!'
   email_from = settings.EMAIL_HOST_USER
   recipient_list = ['jobanputrakavya18@gmail.com','shahyashvi3010@gmail.com'] 
   send_mail(subject, message, email_from, recipient_list)
   return HttpResponse("mail sent")

class AddService(CreateView):
    model = Services
    fields = ['service_name','service_description']
    template_name = 'services/add_service.html'
    success_url = '/users/view'

class ViewService(ListView):
    model = Services
    fields = ['service_name','service_description']
    services = model.objects.all()
    template_name = 'services/view_service.html'
    success_url = '/users/'

class DetailService(DetailView):
    model = Services
    context_object_name = 'service'
    template_name = 'services/detail_service.html'

class DeleteService(DeleteView):
    model = Services
    template_name = "services/delete.html"
    success_url = '/users/view'


class UpdateService(UpdateView):
    model = Services
    fields = ['serivce_name']
    template_name = 'services/update_service.html'
    success_url = '/users/view'
