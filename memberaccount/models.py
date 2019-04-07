from django.conf import settings
from django.db import models
from django.utils import timezone



class Member_share(models.Model):    
    date_posted = models.DateTimeField(default=timezone.now)
    document_no = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    debit_amount = models.CharField(max_length=200)
    credit_amount = models.CharField(max_length=200)
    balance = models.CharField(max_length=200)
    approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
    date_approved = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.description