from django.db import models


class Tweet(models.Model):
    tweet_text = models.CharField(max_length=140)
    tweet_user = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date')
