from django.db import models

class EntityModel(models.Model):
    legal_name = models.CharField(max_length=200)
    legal_code = models.CharField(max_length=8)
    reg_date = models.DateField()
    legal_agent = models.CharField(max_length=120)
    legal_fund = models.FloatField()
    legal_form = models.CharField(max_length=120)
    legal_activity = models.CharField(max_length=300, null=True, blank=True)
    legal_address = models.CharField(max_length=300, null=True, blank=True)
    legal_phone = models.CharField(max_length=24, null=True, blank=True)
    date_added = models.DateTimeField()