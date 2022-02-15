from re import template
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, UserProfileForm
from news.models import NewsStory

# Create your views here.
class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class UserHomePageView(UpdateView):
    model = CustomUser
    form_class = UserProfileForm
    success_url = reverse_lazy('users:userHomePage')
    template_name = 'users/userHomePage.html'

    def get_object(self, queryset=None):
        return self.request.user

class ProfilePageView(DetailView): 
    model = CustomUser
    template_name = "users/profile.html"
    context_object_name = 'profilePage'