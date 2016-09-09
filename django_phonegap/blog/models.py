from django.db import models
from django.conf import settings

# Create your models here.
class Posting(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.post[:10]

    class Meta:
        ordering = ["-updated_at","-created_at"]