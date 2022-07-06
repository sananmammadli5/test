from . import views
from django.urls import path

urlpatterns = [
    path('signup',views.Signup.as_view(),name='signuppage'),
]