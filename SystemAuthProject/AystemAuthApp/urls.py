from django.urls import path
from AystemAuthApp import views
urlpatterns = [
    path("",views.user_signup, name = 'signup'),
    path("login/",views.user_login, name = 'login'),
    path("profile/",views.user_profile, name = 'profile'),
    path("logout/",views.user_logout, name = 'logout'),
    path("passchange/",views.passwordchange, name = 'passchange'),
    path("setpass/",views.setpassword, name = 'setpassword'),
]
