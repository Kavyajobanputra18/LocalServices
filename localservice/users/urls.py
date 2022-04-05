from django.contrib import admin
from django.urls import path,include
from users import views
from .views import SProviderSignUpView,SFinderSignUpView,LoginView,LogoutView
from .views import AddService,ViewService,DeleteService,UpdateService,DetailService
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

]