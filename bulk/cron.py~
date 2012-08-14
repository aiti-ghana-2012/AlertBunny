from django_cron import cronScheduler, Job
from schedulesms import schedule_sms


print 'hello this is django cron'

class sendmessage(Job):
      run_every = 1


      def job(self):
          print 'job processing '
          schedule_sms()






cronScheduler.register(sendmessage)
