"""newvikasproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.welcomepage,name="welcomepage"),
    path('signin',views.welcomepagesignin,name="welcomepagesignin"),
    path('verifying',views.welcomepageverifying,name="welcomepageverifying"),
    path('confirmation',views.welcomepageconfirmation,name="welcomepageconfirmation"),
    path('register1/<str:email>',views.welcomepageregister1,name="welcomepageregister1"),
    path('login',views.welcomepagelogin,name="welcomepagelogin"),
    path('userlogin',views.userlogin,name="userlogin"),
    path('forgotpass',views.forgotpass,name="forgotpass"),
    path('forgotpassword',views.forgotpassword,name="forgotpassword"),
    path('forgotemailpassword',views.forgotemailpassword,name="forgotemailpassword"),
    path('verifyforgotemailpassword',views.verifyforgotemailpassword,name="verifyforgotemailpassword"),
    path('resetpassword',views.resetpassword,name="resetpassword"),
    path('changepassword',views.changepassword,name="changepassword"),

]
