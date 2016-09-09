from django.db import models
from django.conf import settings

# Create your models here.
class Posting(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    #post = models.CharField(max_length=500)
    title = models.CharField(max_length=200, default='Title')
    url = models.URLField(max_length=400, default="http://youtube.com/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title[:10]

    class Meta:
        ordering = ["-updated_at","-created_at"]