from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="index_http"),
    path("signup",views.signup,name='signup')
]
