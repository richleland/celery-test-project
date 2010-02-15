from django.db import models
from django.core.urlresolvers import reverse

class Person(models.Model):
    date_of_birth = models.DateField()
    prefix = models.CharField(max_length=10, blank=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)
    suffix = models.CharField(max_length=10, blank=True)
    can_drink = models.BooleanField(default=False, editable=False)
    full_name = models.TextField(blank=True, editable=False)
    
    class Meta:
        verbose_name_plural = "people"
    
    def __unicode__(self):
        return self.full_name or self.last_name
    
    def call_delay(self):
        url = reverse('call-celery-delay', kwargs={'person_id': self.id})
        return '<a href="%s">Call Celery Delay</a>' % url
    call_delay.allow_tags = True
