from re import template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, UserProfileForm

# Create your views here.
class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class UserHomePageView(UpdateView):
    form_class = UserProfileForm
    success_url = reverse_lazy('userHomePage')
    template_name = 'users/userHomePage.html'