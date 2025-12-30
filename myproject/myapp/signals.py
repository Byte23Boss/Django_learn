from django.db.models.signals import post_save # in django.db.models,.signals
from django.dispatch import receiver # from dispatch model importing receiver
# 
from .models import Student_Signals 


@receiver(post_save, sender = Student_Signals) #checks 1st the data is saved in students_signals , after data is inserted post_save signals triggers the receiver method
def Student_created(sender,instance,created,**kwargs): # kwargs --> keywordargs for adding extra data for below function like adding a keyword ,in instance , data fileds like name,age are stored
    if created: # checks if new record is inserted , boradcast mail example
        print(f'Student Created: {instance.name}')
#go to apps.py and refer