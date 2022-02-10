from django.urls import path
from .views import CreateAccountView, UserHomePageView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(),
    name = 'createAccount'),
    path('user-homepage/', UserHomePageView.as_view(),
    name = 'userHomePage'),
]