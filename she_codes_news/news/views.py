from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy, reverse
from .models import NewsStory
from .forms import StoryForm
from django.http import HttpResponseRedirect


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all()[:4]
        context['all_stories'] = NewsStory.objects.all()
        return context



class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'


class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class EditStoryView(generic.UpdateView):
    model = NewsStory
    fields = ['title', 'category', 'image', 'content']
    context_object_name = 'editStoryForm'
    template_name = 'news/edit_story.html'
    success_url = reverse_lazy('news:index')



class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    template_name = 'news/delete_story.html'
    success_url = reverse_lazy('news:index')



def LikeStoryView(request, pk):
    story = get_object_or_404(NewsStory, id=request.POST.get('story_id'))
    story.likes.add(request.user)

    return HttpResponseRedirect(reverse('story',args=[str(pk)]))
