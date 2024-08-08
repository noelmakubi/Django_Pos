from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup, name='signup'),

    path('signin',views.signin, name='signin'),

    path('passwordrec', views.passwordrec, name='passwordrec')
]
