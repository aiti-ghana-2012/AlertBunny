from dj_simple_sms.models import SMS
from models import Message


from datetime import date





def schedule_sms():
    message = Message.objects.filter(scheduledate__gte=date.today(),sent=False)
    for datetoschedule in message:
           message_to_send = SMS(to_number=datetoschedule.receiver, from_number=datetoschedule.sender, body=datetoschedule.body)
           message_to_send.send()
           datetoschedule.sent=True
           datetoschedule.save()
    
    return  'sent'

