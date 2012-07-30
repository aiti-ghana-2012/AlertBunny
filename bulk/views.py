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

'''
beginning sms
'''

class SMSform(ModelForm):
      class Meta:
              model=Message
              #exclude=['customer']
              

    
@csrf_exempt
def sample_send_sms(request):
    if request.user.username == '':
	return HttpResponseRedirect('/reg/login')	
    if request.method =='POST':
        form=SMSform(request.POST)
        if form.is_valid():
            form.save()
          
            message=form.cleaned_data['body']
            receiver=form.cleaned_data['receiver']
            sender=form.cleaned_data['sender']
      
            message_to_send = SMS(to_number=receiver, from_number=sender, body=message)
            message_to_send.send()
            return  render_to_response('bulk/base_sentsms.html',{'form':form})
    else:
        form=SMSform()
        print 2
    return  render_to_response('bulk/base_sendsms.html',{'form':form,'user':request.user})
