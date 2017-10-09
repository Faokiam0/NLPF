from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import FortuneForm, ConnexionForm
from .models import Fortune

class IndexView(generic.ListView):
    template_name = 'fortune/index.html'
    context_object_name = 'latest_fortune_list'

    def get_queryset(self):
        return Fortune.objects.order_by('-pub_date')

class TopView(generic.ListView):
    template_name = 'fortune/results.html'
    context_object_name = 'latest_fortune_list'

    def get_queryset(self):
        return Fortune.objects.order_by('-score')[:30]

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

def up(request, fortune_id):
    fortune = get_object_or_404(Fortune, pk=fortune_id)
    fortune.score += 1
    if request.user.is_authenticated:
        fortune.score += 1
    fortune.save()
    return HttpResponseRedirect(reverse('fortune:detail', args=(fortune.id,)))

def down(request, fortune_id):
    fortune = get_object_or_404(Fortune, pk=fortune_id)
    fortune.score -= 1
    if request.user.is_authenticated:
        fortune.score -= 1
    fortune.save()
    return HttpResponseRedirect(reverse('fortune:detail', args=(fortune.id,)))

def connect(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'fortune/login.html', locals())

def deconnect(request):
    logout(request)
    return HttpResponseRedirect(reverse('fortune:connect'))

def register(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(username, username,password)
            if user:
                login(request, user)
            else:
                error = True
    else:
        form = ConnexionForm()
    return render(request, 'fortune/register.html', locals())