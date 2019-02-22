from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.proff,name = 'landing'),
    url('^projects/$', views.proj, name = 'proj'),
    url('^skills/$', views.skill, name = 'skills'),
    url('^contacts/$', views.contact, name = 'contacts'),
]


