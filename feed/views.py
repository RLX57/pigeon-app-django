from django.shortcuts import render
from feed.forms import TweetForm
from django.utils import timezone
from feed.models import Tweet


def index(request):
    latest_tweet_list = Tweet.objects.order_by('-pub_date')[:20]
    form = TweetForm(request.POST)

    if form.is_valid():
        t = form.save(commit=False)
        t.pub_date = timezone.now()
        t.save()

    context = {'latest_tweet_list': latest_tweet_list, 'form': form}
    return render(request, 'feed/index.html', context)


def tweet(request):
    form = TweetForm(request.POST)
    tweet = request.POST.get('message', '')
    user = request.POST.get('user', '')

    if tweet and user:
        tweetsend = Tweet(
            tweet_text=tweet, tweet_user=user, pub_date=timezone.now())
        tweetsend.save()

    return render(request, 'feed/tweet.html', {'form': form})
