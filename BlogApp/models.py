from django.db import models

class Post(models.Model):
    subject = models.CharField(max_length=100)
    text = models.TextField(max_length=2000)
    datePosted = models.DateTimeField()
    def __str__(self):
        return self.subject
