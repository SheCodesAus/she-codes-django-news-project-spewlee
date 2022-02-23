from django.forms import ModelForm
from .models import NewsStory

category_options = [("Python","Python"), ("Django","Django"),("HTML","HTML"), ("CSS","CSS"), ("JavaScript","JavaScript"), ("React","React"), ("General","General"), ("Career","Career")]

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ["title", "category", "content", "image"]
    