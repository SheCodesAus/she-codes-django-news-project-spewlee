from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView
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
    model = CustomUser
    form_class = UserProfileForm
    success_url = '/success/'
    success_messsage = "Your profile was updated successfully!"
    template_name = 'users/userHomePage.html'

    def get_object(self, queryset=None):
        return self.request.user

class ProfilePageView(DetailView): 
    model = CustomUser
    template_name = "users/profile.html"
    context_object_name = 'profilePage'