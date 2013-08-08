Setting up the app

Assuming you have Django installed and this app installed
1. python manage.py syncdb
2. Add url(r'^contacts/', include('contacts.urls'))
