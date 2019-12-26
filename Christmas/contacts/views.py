from django.shortcuts import render,redirect
from contacts.models import  Contact
# Create your views here.
from django.contrib import messages

def contact(request):
    if request.method=='POST':
        listing_id=request.POST['listing_id']
        listing=request.POST['listing']
        email=request.POST['email']
        phone=request.POST['phone']
        name=request.POST['name']
        message=request.POST['message']
        user_id=request.POST['user_id']
        realtor_email=request.POST['realtor_email']
        contact = Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
        contact.save()
        messages.success(request,'Your request has been submitted , a realtor will be back ')

        return redirect('/listings/'+listing_id)