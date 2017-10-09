from django.conf.urls import url

from . import views

app_name = 'fortune'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^new/$', views.FortuneCreate.as_view(), name='new'),
    url(r'^results/$', views.TopView.as_view(), name='results'),
    url(r'^(?P<fortune_id>[0-9]+)/up/$', views.up, name='up'),
    url(r'^(?P<fortune_id>[0-9]+)/down/$', views.down, name='down'),
    url(r'^connect/$', views.connect, name='connect'),
    url(r'^deconnect/$', views.deconnect, name='deconnect'),
    url(r'^register/$', views.register, name='register'),
]