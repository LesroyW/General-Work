from django.shortcuts import render
from django.http import HttpResponseRedirect
from Django.core.urlresolvers import reverse

from .models import Topic
from .forms import TopicForm
# Create your views here.

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_vaild():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
        