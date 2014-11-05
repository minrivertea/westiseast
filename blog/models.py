from django.db import models
from django.core.urlresolvers import reverse


class Photo(models.Model):
    image = models.ImageField(upload_to='photos')
    slug = models.SlugField(max_length=80)
    date_added = models.DateField()
    is_featured = models.BooleanField(default=False)
    description = models.TextField()
    title = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        url = reverse('photo', args=[self.slug])
        return url



class BlogEntry(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=80)
    date_added = models.DateField()
    content = models.TextField()
    is_draft = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.slug
        
    def get_absolute_url(self):
        return "/blog/%s/" % self.slug
     
    def get_content(self):
        return self.summary
        
    def get_type(self):
        return "blog"
    
        
class CoolShit(models.Model):
    link = models.URLField()
    date_added = models.DateField()
    TYPE_CHOICES = (
        ('fire', 'fire'),
        ('camera', 'camera'),
    )
    type = models.CharField(max_length=40, choices=TYPE_CHOICES)
    
    description = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.title
    
    def get_content(self):
        return self.description

    def get_type(self):
        return self.type
    
        


