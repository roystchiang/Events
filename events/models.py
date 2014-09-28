from django.db import models

# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    map_lon = models.FloatField(blank=True, null=True)
    map_lat = models.FloatField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='events', blank=True, null=True)
    def __unicode__(self):
        return unicode(self.name)