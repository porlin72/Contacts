from django.conf.urls import patterns, include, url

urlpatterns = patterns('contacts.views',
    url(r'^somewhere/$', 'somewhere', name='somewhere'),
    url(r'^create/$', 'create_contact', name='create contact'),
    url(r'^mycontacts/$', 'display_contacts', name='my contacts'),
    url(r'^contacts_to_delete/$', 'display2_contacts', name='selection of contacts'),
    url(r'^editcontact/(?P<contact_id>\d+)/$', 'edit_contact', name='edit contact'),
    url(r'^deletecontact/(?P<contact_id>\d+)/$', 'delete_contact', name='delete contact'),
    url(r'^homepage/$', 'homepage', name='home'),
    url(r'^about/$', 'about', name='about'),
    )