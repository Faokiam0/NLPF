from django.http import HttpResponse
from django.views import generic

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

class FortuneCreate(generic.CreateView):
    model = Fortune
    form_class = FortuneForm
    succes_url = '/'
    template_name = 'fortune/new.html'
    def form_valid(self, form):
        form.save()
        return super(FortuneCreate, self).form_valid(form)