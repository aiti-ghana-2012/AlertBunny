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

from models import Message,Contact,Group,Servicelog,Customer

from datetime import date

'''
beginning sms
'''

class SMSform(ModelForm):
      class Meta:
              model=Message
              exclude=['sent','customer','optout']




@csrf_exempt
def send_sms(request,uname):
    customers=Customer.objects.get(username=uname)

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
This is the form for the schedule page
'''
class Scheduleform(ModelForm):
      class Meta:
              model=Message
              exclude=['sent','customer','optout']
        
      



#schedule sms function

@csrf_exempt
def schedule_sms(request):
    if request.user.username == '':
	return HttpResponseRedirect('/reg/login')

    if request.method =='POST':
        form=Scheduleform(request.POST)
        print 2
        if form.is_valid():
            date=form.cleaned_data['body']
              
            form.save()
            return  render_to_response('bulk/base_sentsms.html',{'form':form})
          
    else:
        form=Scheduleform()
        return  render_to_response('bulk/base_schedulesms.html',{'form':form,'user':request.user})





'''
opt out function
'''




'''
 from django.core.mail import send_mail
    send_mail(subject, message, sender, recipients)

'''
class optoutform(ModelForm):
      class Meta:
              model=Message
              exclude=['scheduledate','sent','customer','sender','receiver','body','subject']
      

def optout(request):
    message=Message.objects.filter(scheduledate__gte=date.today(),sent=False)
    print message
    form=optoutform()
    
    context=Context({'message':message,'user':request.user,'form':form})
    return  render_to_response('bulk/base_optout.html',context)



'''
creating customer profile form for editing
'''


class Customerform(ModelForm):
      class Meta:
              model=Customer
              

@csrf_exempt
def customerprofile(request,id):
    customers=Customer.objects.get(pk=id)
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




@csrf_exempt
def schedule(request):
    return  render_to_response('bulk/base_schedulesms.html')


def aboutUs(request):
    return  render_to_response('bulk/base_abtUs.html',{'user':request.user})
    
