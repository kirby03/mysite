from django.db import models
from django.utils import timezone
# Create your models here.

class Blog(models.Model):
    blog_text = models.CharField(max_length=200, )
    pub_date = models.DateTimeField('date published', default=timezone.now())
    
    def __str__(self):
        return self.blog_text