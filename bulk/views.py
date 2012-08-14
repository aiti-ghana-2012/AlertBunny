# Create your views here.


from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader


from django import  forms 
from django.forms import ModelForm,TextInput
from django.contrib.auth.forms import User
from dj_simple_sms.models import SMS
from django.contrib.auth.decorators import login_required

from models import Message,Contact,Group,Servicelog,Customer

from datetime import date

'''
beginning sms
'''

class SMSform(ModelForm):
      class Meta:
              model=Message
              exclude=['sent','customer','optout','username','group']
              #group= forms.ModelMultipleChoiceField(queryset=Group.objects.all())



@csrf_exempt
@login_required
def send_sms(request):
    customers=Customer.objects.get(username=request.user)

    if request.user.username == '':
	return HttpResponseRedirect('/reg/login')

    if request.method =='POST':
        message=Message(customer=customers,username=request.user)

        form=SMSform(request.POST,instance=message)
        if form.is_valid():
            form.save()
            '''
            message=form.cleaned_data['body']
            receiver=form.cleaned_data['receiver']
            sender=form.cleaned_data['sender']
            listnumbers=receiver.split(',')
            for  receivers in listnumbers:
               
               message=form.cleaned_data['body']
               receiver=form.cleaned_data['receiver']
               sender=form.cleaned_data['sender']
               message_to_send = SMS(to_number=receivers, from_number=sender, body=message)
               message_to_send.send()
'''
            return  render_to_response('bulk/base_sentsms.html',{'form':form})
          
    else:
        form=SMSform()
    return  render_to_response('bulk/base_sendsms.html',{'form':form,'user':request.user})







'''
This is an opt-out form .This provides a form with optout option as the very first form.
This comes with the other form because we believe that it is possible for the user to 
change decision

'''

class Optoutform(ModelForm):
      class Meta:
              model=Message
              exclude=['sent','customer']
              fields = ("optout","sender","receiver","body","scheduledate")
      
'''
Our optout function filters the message model to obtain all user with 
his/her username equal to request.user and has his messages not sent but has still not opted out 
'''
@csrf_exempt
@login_required
def optout(request):
    message=Message.objects.filter(username=request.user,sent=False,optout=False)
    form=Optoutform()
    
    context=Context({'message':message,'user':request.user,'form':form})
    return  render_to_response('bulk/base_optout.html',context)

@csrf_exempt 
@login_required
def editoptout(request,id):
    message=Message.objects.get(pk=id)
    if request.method =='POST':
        form=Optoutform(request.POST,instance=message)
        if form.is_valid():
            form.save()
            context=Context({'form':form,'user':request.user})
            return HttpResponseRedirect('/bulk/sendsms')
    else:
        form=Optoutform(instance=message)
        context=Context({'form':form,'user':request.user})
    return  render_to_response('bulk/base_editoptout.html',context)

'''
creating customer profile form for editing
'''


class Customerform(ModelForm):
      class Meta:
              model=Customer
              exclude=['activation_key','key_expires','username']
              

@csrf_exempt
@login_required
def profile(request):
    customers=Customer.objects.get(username=request.user)
    if request.method =='POST':
        form=Customerform(request.POST,instance=customers)
        if form.is_valid():
            form.save()
            context=Context({'form':form,'user':request.user})
            return HttpResponseRedirect('/bulk/sendsms')
    else:
        form=Customerform(instance=customers)
    context=Context({'form':form,'user':request.user})
    return  render_to_response('bulk/base_customerprofile.html',context)


@csrf_exempt
@login_required 
def sent_sms(request):
    message=Message.objects.filter(username=request.user,sent=True).order_by('-scheduledate')
    print message

    context=Context({'message':message,'user':request.user})
    return  render_to_response('bulk/base_sentmessage.html',context)



@csrf_exempt
@login_required 
def editmessage(request,id):
    message=Message.objects.get(pk=id)
    if request.method =='POST':
        form=SMSform(request.POST,instance=message)
        if form.is_valid():
            form.save()
            context=Context({'form':form,'user':request.user})
            return HttpResponseRedirect('/bulk/sendsms')
    else:
        form=SMSform(instance=message)
        context=Context({'form':form,'user':request.user})
    return  render_to_response('bulk/base_messageedit.html',context)
'''

def scheduledmessage(request,uname):
    message=Message.objects.get(username=uname)
    if request.method =='POST':
        form=SMSform(request.POST,instance=message)
        if form.is_valid():
            form.save()
            context=Context({'form':form,'user':request.user})
            return HttpResponseRedirect('/bulk/sendsms')
    else:
        form=SMSform(instance=message)
        context=Context({'form':form,'user':request.user})
    return  render_to_response('bulk/base_messageedit.html',context)

'''

@csrf_exempt
@login_required
def scheduled(request):
    message=Message.objects.filter(username=request.user,sent=False,optout=False)

    context=Context({'message':message,'user':request.user})
    return  render_to_response('bulk/base_scheduledmessage.html',context)



@csrf_exempt
@login_required
def grouplist(request):
    group=Group.objects.filter(username=request.user)

    context=Context({'group':group,'user':request.user})
    return  render_to_response('bulk/base_group.html',context)


@csrf_exempt
@login_required
def groupcontact(request,id):
    group=Group.objects.get(pk=id)
    contacts=group.contact.all()
    #contacts=contact.contact.filter(groupname=contact.groupname)
    context=Context({'contact':contacts,'user':request.user})
    return  render_to_response('bulk/base_groupcontact.html',context)
'''
'''


class Contactform(ModelForm):
      class Meta:
            model=Contact
            exclude=['username','group']
             

@csrf_exempt
@login_required
def addcontact(request,id):
    if request.method=='POST':
       groups=Group.objects.get(pk=id)
       contact=Contact(group=groups,username=request.user)
       form=Contactform(request.POST,instance=contact)
       if form.is_valid():
          
           form.save()
           
           return HttpResponseRedirect('/bulk/groupcontacts/' +str(id) )
    else:
        form=Contactform()
    context=Context({'form':form,'user':request.user})

    return  render_to_response('bulk/base_addcontacts.html',context)

'''
This is our add group function 
The add group function is suppose help the user add new groups and then provides contacts 
for that groups.
'''

#group form
class Groupform(ModelForm):
      class Meta:
              model=Group
              exclude=['customer','contact','username']




@csrf_exempt
@login_required
def addgroup(request):
    
    customers=Customer.objects.get(username=request.user)
    if request.method=='POST':
       group=Group(customer=customers,username=request.user)
       form=Groupform(request.POST,instance=group)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect('/bulk/group')
    else:
        form=Groupform()
        context=Context({'form':form,'user':request.user})

    return  render_to_response('bulk/base_addgroup.html',context)


@csrf_exempt
@login_required
def groupcontacts(request,id):
    groups=Group.objects.get(pk=id)
    contacts=Contact.objects.filter(group=groups)

    context=Context({'contacts':contacts,'user':request.user,'group':groups})
    return  render_to_response('bulk/base_groupcontact.html',context)
    



@csrf_exempt
def aboutUs(request):
    return  render_to_response('bulk/base_abtUs.html',{'user':request.user})

@csrf_exempt
def buyCredit(request):
    return  render_to_response('bulk/base_buycrdt.html',{'user':request.user})

@csrf_exempt
def contact_Us(request):
    return  render_to_response('bulk/base_contactUs.html',{'user':request.user})

@csrf_exempt
def faqs(request):
    return  render_to_response('bulk/base_faqs.html',{'user':request.user})

@csrf_exempt
def abFeatures(request):
    return  render_to_response('bulk/features.html',{'user':request.user})

