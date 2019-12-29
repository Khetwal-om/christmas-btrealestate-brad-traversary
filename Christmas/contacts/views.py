from django.shortcuts import render,redirect
from contacts.models import  Contact
# Create your views here.
from django.contrib import messages
from django.core.mail import send_mail

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

        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'You have already made an enquiry for this listing')
                return redirect('/listings/' + listing_id)

        contact = Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
        contact.save()

        #email

        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for '+listing+'sign into admin panel for further information',
            'lotolopezlp7@gmail.com',
            [realtor_email,'khetwalom@gmail.com'],
            fail_silently=False
        )

        messages.success(request,'Your request has been submitted , a realtor will be back ')

        return redirect('/listings/'+listing_id)