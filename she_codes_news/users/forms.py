from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class UserProfileForm(UserChangeForm): #Come back to this. Not sure if "UserChangeForm" is the correct thing to pass
    
    class Meta:
        model: CustomUser
        fields = ['name', 'profile_pic', 'github_url', 'linkedin_url', 'bio' ]
