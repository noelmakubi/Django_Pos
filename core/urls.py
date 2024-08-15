from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('password_recovery', views.passwordrec, name='passwordrec'),
    path('index',views.index,name='index' ),
    path('add_product', views.add_product,name='add_product'),
    path('list_product', views.list_product, name='list_product'),
]
