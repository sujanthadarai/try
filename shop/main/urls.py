from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name="index"),
    path("register/",register,name="register"),
    path("login/",log_in,name="log_in"),
    path('logout/',log_out,name="log_out"),
    path('search',search_form,name="search_form")
]
