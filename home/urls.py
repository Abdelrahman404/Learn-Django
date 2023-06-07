
from django.urls import path
from home import views

urlpatterns = [
 
    path('', views.HomeView.as_view()),
    path('signup', views.SignupView.as_view(), name='signup')

]
