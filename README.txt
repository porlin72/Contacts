Contacts simple for adding name and phone number
Requires the userprofile app for registration and login of a user

Setting up the app

Assuming you have Django and Python installed
1. python manage.py syncdb
2. Add url(r'^contacts/', include('contacts.urls')), 
       url(r'^user/', include('userprofile.urls'))
3. Add the app name to your settings.py file in your project
4. Add the mytemplates folder to settings.py file
