from models import Contact
from django import forms
from forms import ContactForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User

def somewhere(request):
    return render(request, 'contacts/somewhere.html')
        
def create_contact(request):
    if request.user.is_authenticated():
        user = request.user
        
        if request.method == 'POST':    
            form = ContactForm(request.POST)
            
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = user
                obj.save()
                
                return HttpResponseRedirect('/contacts/mycontacts/')
        else:
            form = ContactForm(initial={'user' : User})
            
        args = {}
        args.update(csrf(request))
        
        args['form'] = form
        
        return render_to_response('contacts/create_contact.html', args)
    else:
        c = {}
        c.update(csrf(request))
        return render_to_response('registration/login.html', c)
    
def display_contacts(request):
    if request.user.is_authenticated():
        contacts = Contact.objects.filter(user=request.user)
        return render_to_response('contacts/display_contacts.html', { 'contacts' : contacts })
        
def display2_contacts(request):
    if request.user.is_authenticated():
        contacts = Contact.objects.filter(user=request.user)
        return render_to_response('contacts/display2_contacts.html', { 'contacts' : contacts })        
    
def homepage(request):
    return render_to_response('homepage.html')
    
def about(request):
    return render_to_response('about.html')
   
def edit_contact(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    
    if request.method == 'POST':
        contact_form = ContactForm(request.POST, instance = contact)
        
        if contact_form.is_valid():
            contact_form.save()
            
            return HttpResponseRedirect('/contacts/mycontacts/', { 'contacts' : contact } )
    else:
        contact_form = ContactForm(instance=contact)
        
        args = {}
        args.update(csrf(request))
        
        args['contact_form'] = contact_form
        
        return render_to_response('contacts/edit_contact.html', args)
        
def delete_contact(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    contact.delete()
    return render_to_response('contacts/delete_contact.html')