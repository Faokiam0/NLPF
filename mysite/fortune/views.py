from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from datetime import datetime

from .forms import FortuneForm
from .models import Fortune

class IndexView(generic.ListView):
    template_name = 'fortune/index.html'
    context_object_name = 'latest_fortune_list'

    def get_queryset(self):
        return Fortune.objects.order_by('-pub_date')[:30]

class DetailView(generic.DetailView):
    model = Fortune
    template_name = 'fortune/detail.html'

class FortuneCreate(generic.FormView):
    model = Fortune
    form_class = FortuneForm
    success_url = '/fortune/'
    template_name = 'fortune/new.html'
    def form_valid(self, form):
        self.object = form.save(commit=True)
        self.object.score = 0
        self.object.pub_date = datetime.now()
        self.object.save()
        return super(FortuneCreate, self).form_valid(form)