from django import forms
from django.forms import ModelForm
from .models import NewsStory

category_options = [("Python","Python"), ("Django","Django"),("HTML","HTML"), ("CSS","CSS"), ("JavaScript","JavaScript"), ("React","React"), ("General","General"), ("Career","Career")]

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'content', 'category', 'image']
        
        widgets = {
            'category':forms.Select(choices=category_options, attrs={'class':'form-control'}),
        #     'pub_date': forms.DateInput(format=('%m/%d/%Y'),
        #     attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }