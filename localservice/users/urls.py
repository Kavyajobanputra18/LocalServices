from django.contrib import admin
from django.urls import path,include
from users import views
from .views import SProviderSignUpView,SFinderSignUpView,LoginView,LogoutView
urlpatterns = [
    path('',views.index ,name= 'index'),
    path('listing/',views.listing ,name= 'listing'),
    path('contact/',views.contact ,name= 'contact'),
    path('category/',views.category ,name= 'category'),
    path('sprovidersignup/',SProviderSignUpView.as_view(), name = 'sprovider'),
    path('sfindersignup/',SFinderSignUpView.as_view(), name = 'sfinder'),
    path('login/',LoginView.as_view(), name = 'login'),
    path('logout/',LogoutView.as_view(), name = 'logout'),
    path('sendmail/',views.sendmail, name='send_mail' ),

]