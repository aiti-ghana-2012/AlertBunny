# Create your views here.


from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt


from django import  forms 
from django.forms import ModelForm
from django.contrib.auth.forms import User
from dj_simple_sms.models import SMS

from models import Message,Contact,Group,Servicelog

from datetime import date

'''
beginning sms
'''

class SMSform(ModelForm):
      class Meta:
              model=Message
              exclude=['scheduledate','sent','customer']

@csrf_exempt         
def send_scheduled_sms(request):
    message = Message.objects.filter(scheduledate__gte=date.today())
    for datetoschedule in message:
        if datetoschedule.sent==False:
           message_to_send = SMS(to_number=datetoschedule.receiver, from_number=datetoschedule.sender, body=datetoschedule.body)
           message_to_send.send()
           datetoschedule.sent=True
           datetoschedule.save()
    
    return  HttpResponse(str(message))

  
@csrf_exempt
def send_sms(request):

    if request.method =='POST':
        
        form=SMSform(request.POST)
        if form.is_valid():
            form.save()
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
            return  render_to_response('bulk/base_sentsms.html',{'form':form})
    else:
        form=SMSform()
    return  render_to_response('bulk/base_sendsms.html',{'form':form})


def schedule(request):
    return  render_to_response('bulk/base_schedulesms.html')
    




