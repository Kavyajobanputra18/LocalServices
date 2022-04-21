
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
from django.contrib.auth.decorators import login_required

#for email
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def index1(request):
    return render(request, 'users/loginafterindex.html')

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
        username=form.cleaned_data.get('username')
        password1 = form.cleaned_data.get('password1')
        dict = {'username':username, 'password1': password1}
        subject, from_email, to = 'subject', settings.EMAIL_HOST_USER, form.cleaned_data.get('email')
        
        html_content=render_to_string('users/email.html', dict)
        text_content = strip_tags(html_content)

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()      
        return redirect('/users/login/')

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
        username=form.cleaned_data.get('username')
        password1 = form.cleaned_data.get('password1')
        dict = {'username':username, 'password1': password1}
        subject, from_email, to = 'subject', settings.EMAIL_HOST_USER, form.cleaned_data.get('email')
        html_content=render_to_string('users/email.html', dict)
        text_content = strip_tags(html_content)
        msg= EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()      
        
        return redirect('/users/login/')

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
    context_object_name='services'
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


# def profile(request):
#     return render(request, 'users/profile.html')

# def Profile(request,pk):
#     user = User.objects.get(pk=pk)
#     servicefinder = ServiceFinder.objects.get(user_id=user)
#     return render(request, 'users/profile.html',{'user':user,'servicefinder':servicefinder})

# def UpdateProfile(request,pk):
#     user = User.objects.get(pk=pk)
#     if user.role == "ServiceFinder":
#         sfinder = ServiceFinder.objects.get(user_id=user)
#         sfinder.address = request.POST['address']
#         sfinder.city = request.POST['city']
#         sfinder.state = request.POST['state']
#         sfinder.pincode = request.POST['pincode']
#         sfinder.save()
#         url = f'/profile/{pk}'
#         return redirect(url)

@login_required
def profile(request):
    return render(request, 'users/profile.html')