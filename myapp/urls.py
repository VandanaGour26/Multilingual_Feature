#from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),

    # Login Page
   # path('login/', LoginView.as_view(template_name='login.html'), name='login'), 
    # Logout 
   # path('logout/', LogoutView.as_view(next_page='home'), name='logout'), 

    # register Page
   # path('login/', LoginView.as_view(template_name='register.html'), name='login'),  
    # Go to login page
   # path('logout/', LogoutView.as_view(next_page='login_user'), name='logout'), 

    # set login urls
    path('login_user',views.login_user,name="login_user"),

    # set logout urls
    path('logout_user',views.logout_user,name="logout_user"),

   # set registration page
    path('register/',views.register,name="register"),

   #set language
   path('set_language/', views.set_language, name='set_language'),


]
