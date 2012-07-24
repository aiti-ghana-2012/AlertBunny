from django.db import models
from django.contrib import admin

# Create your models here.
'''
Person class
Customer class
Contact class
Message class
Service_log class

'''

class Person(models.Model):
      fistname = models.CharField(max_length=30)

      lastname = models.CharField(max_length=30)

      email = models.EmailField(max_length=254,unique=True)

      mobilenumber=models.PositiveIntegerField(blank=True)
      

      def __unicode__(self):
             return self.email






class Customer(models.Model):
      dateofbirth=models.DateField()

      gender=models.CharField(max_length=30)

      companyname=models.CharField(max_length=30,unique=True)

      postalAddress=models.TextField()


      

      def __unicode__(self):
             return self.companyname





class Message(models.Model):
      subject=models.CharField(max_length=30)

      sender=models.CharField(max_length=30)

      receiver=models.CharField(max_length=30)

      scheduledate=models.DateField()

      customer=models.ForeignKey(Customer,related_name='messages')

      def sendSms():
          pass


      def createmessagelog():
          pass
      def usetemplate():
          pass

      def __unicode__(self):
             return self.subject








class Contact(models.Model):

      groupname=models.CharField(max_length=100)



      customer=models.ForeignKey(Customer,related_name='contacts')
      
      def viewcontact():
          pass
      def updatecontact():
          pass
      def deletecontact():
          pass
      def saveContact():
          pass

      def __unicode__(self):
           return self.groupname




class Servicelog(models.Model):
      smsstatus=models.TextField()

      def createservicelog():
          pass
      


      def __unicode__(self):
             return self.smsstatus


admin.site.register(Servicelog)

admin.site.register(Message)

admin.site.register(Contact)

admin.site.register(Person)

admin.site.register(Customer)





      
