from django.conf.urls import patterns, include, url

urlpatterns = patterns('userprofile.views',
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^loggedin/$', 'loggedin', name='loggedin'),
    url(r'^invalid/$', 'invalid', name='invalid'),
    url(r'^auth/$', 'auth_view', name='auth_view'),
    url(r'^register/$', 'register', name='register'),
    url(r'^register_success/$', 'register_success', name='sucessful registration'),
    )