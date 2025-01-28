from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="authentication"),
    path("/signin",views.signup,name='signing')
]