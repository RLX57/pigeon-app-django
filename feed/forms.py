from django.forms import ModelForm
from feed.models import Tweet


class TweetForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ['tweet_text', 'tweet_user']
