from django.db import models
from django.contrib.auth.models import User

class Memo(models.Model):
    """
    A memo is a relatively light-weight way of sending notifications
    and messages to registered users. These are less transient than
    Django's built in messaging service, having dates for ordering.
    """
    user = models.ForeignKey(User)
    memo = models.TextField()
    dtsent = models.DateTimeField(auto_now_add=True,editable=False)
    
    def send_by_email(self):
        pass
        
    def send_by_sms(self):
        pass
        
    def __unicode__(self):
        return self.memo
