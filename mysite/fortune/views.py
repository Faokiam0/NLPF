from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Fortune

def index(request):
    latest_fortune_list = Fortune.objects.order_by('-pub_date')[:30]
    context = {'latest_fortune_list': latest_fortune_list}
    return render(request, 'fortune/index.html', context)

def detail(request, fortune_id):
    try:
        fortune = Fortune.objects.get(pk=fortune_id)
    except Fortune.DoesNotExist:
        raise Http404("Fortune does not exist")
    return render(request, 'fortune/detail.html', {'fortune': fortune})