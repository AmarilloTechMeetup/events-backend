from django.db import models
from django.db.models import permalink
from django.utils.timezone import now

# Create your models here.



class Content(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField(help_text="Full HTML allowed. Keep headers at h2 or smaller.")
    slug = models.SlugField(max_length=100, unique=True, help_text="This is the url extension.")
    posted = models.DateTimeField(db_index=True, default=now)
    category = models.ForeignKey('content.Category',blank=True,null=True)
    def __str__(self):
        return '%s' % (self.title)

    @permalink
    def get_absolute_url(self):
        return ('view_post', None, { 'slug': self.slug })
    
class Category(models.Model):
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return '%s' % self.slug

    @permalink
    def get_absolute_url(self):
        return ('view_category', None, { 'slug': self.slug })

class Event(models.Model):
    title= models.CharField(max_length=100, unique=True)
    description=models.TextField(help_text="Full HTML allowed. Keep headers at h2 or smaller.")
    address1= models.CharField(max_length=50)
    address2= models.CharField(max_length=50)
    city= models.CharField(max_length=2)
    #state= models.TextField(help_text="Full HTML allowed. Keep headers at h2 or smaller.")
    #zipcode= models.IntegerField()
    datetime=models.DateTimeField(db_index=True, default=now)
    cost=models.FloatField(default=0.0)
    picture= models.TextField(db_column='data',blank=True)
    
    def __str__(self):
        return '%s' % (self.title)

    @permalink
    def get_absolute_url(self):
        return ('view_post', None, { 'slug': self.slug })
