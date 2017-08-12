from django.db import models
from django.db.models import permalink
from django.utils.timezone import now

# Create your models here.
CONTENT_TYPE = (
    ('blog', 'Blog Post'),
    ('project', 'Project'),
    ('info', 'Info'),
)


class Content(models.Model):
    purpose = models.CharField(max_length=10, choices=CONTENT_TYPE)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, help_text="This is the url extension.")
    body = models.TextField(help_text="Full HTML allowed. Keep headers at h2 or smaller.")
    posted = models.DateTimeField(db_index=True, default=now)
    category = models.ForeignKey('content.Category',blank=True,null=True)
    image = models.CharField(max_length=100, help_text="This is an optional image url used for the header or thumbnail.")
    image.blank=True;
    def __str__(self):
        return '%s, %s' % (self.purpose, self.title)

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

