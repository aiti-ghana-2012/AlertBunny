from dj_simple_sms.models import SMS
from models import Message

from django.utils.timezone import now
import datetime



def schedule_sms():
    message = Message.objects.filter(scheduledate__lt=now(), sent=False, optout=False)
    
    for datetoschedule in message:
           yet_to_receive=datetoschedule.receiver.split(',')
           for receivers in yet_to_receive:
              message_to_send = SMS(to_number=receivers, from_number=datetoschedule.sender, body=datetoschedule.body)
              message_to_send.send()
              datetoschedule.sent=True
              datetoschedule.save()
    
    return  'sent'

