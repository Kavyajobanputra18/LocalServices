from django.contrib import admin
from django.urls import path,include
from users import views
from .views import SProviderSignUpView,SFinderSignUpView,LoginView,LogoutView
from .views import AddService,ViewService,DeleteService,UpdateService,DetailService
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('',views.index ,name= 'index'),
    path('listing/',views.listing ,name= 'listing'),
    path('contact/',views.contact ,name= 'contact'),
    path('category/',views.category ,name= 'category'),
    path('about/',views.about ,name= 'about'),
    path('reviews/',views.reviews ,name= 'reviews'),
    path('sprovidersignup/',SProviderSignUpView.as_view(), name = 'sprovider'),
    path('sfindersignup/',SFinderSignUpView.as_view(), name = 'sfinder'),
    path('login/',LoginView.as_view(), name = 'login'),
    path('logout/',LogoutView.as_view(), name = 'logout'),
    path('sendmail/',views.sendmail, name='send_mail' ),
    path('add/',AddService.as_view(),name='add_service'),
    path('view/',ViewService.as_view(),name='view_service'),
    path('<int:pk>/view/',DetailService.as_view(),name='detail_service'),
    path('<int:pk>/delete/',DeleteService.as_view(),name='delete_service'),
    path('<int:pk>/update/',UpdateService.as_view(),name='update_service'),
    # path('profile/',views.profile,name = 'profile')
    # path('profile/',views.profile,name='profile'),
    #path('updateprofile/<int:pk>',views.UpdateProfile,name='updateprofile'),
    path('index1/',views.index1 ,name= 'index1'),
    path('profile/', profile, name='users-profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)