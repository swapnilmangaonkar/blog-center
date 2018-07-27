from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings


class Question(models.Model):
    question_title = models.CharField(max_length=200)
    question_topic = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    image = models.FileField(null=True,upload_to='pic/')

    def __unicode__(self):
        return unicode(self.user)

    def __str__(self):
        return self.question_title

class post(models.Model):
    written_by = models.ForeignKey(User ,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    published_time = models.DateTimeField(blank=True , null=True)
    image = models.FileField(null=True , upload_to='media/')

    def __unicode__(self):
        return unicode(self.user)

    def publish(self):
        self.published_time = timezone.now()
        self.save()

    def __str__(self):
        return self.title
