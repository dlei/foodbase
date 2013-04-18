from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.register, name='createAccount'),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),

    url(r'^users/profile/$', views.profile, name='profile'),

    url(r'^addRest/$', views.addRest,name='addRest'),
    url(r'^profile/$', views.profile, name = 'profile'),
    url(r'^search/$', views.search, name = 'rateSearch'),
    url(r'^restaurantList/$', views.restaurantList, name = 'restaurantList'),


)