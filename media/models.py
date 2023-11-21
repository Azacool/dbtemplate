from django.db import models
from django.utils.html import mark_safe
class Post(models.Model):
    owner = models.CharField(max_length=30,blank=False)
    image = models.ImageField(null=True,blank=False)
    text = models.TextField(blank=False)
    
    def image_tag(self):
        return mark_safe('<img src="/mediafolder/%s" width="80" height="80" />' % (self.image))

    image_tag.short_description = 'Image'
    
    def __str__(self) -> str:
        return self.text
