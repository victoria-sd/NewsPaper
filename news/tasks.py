import datetime
from celery import shared_task
from celery import shared_task
import time
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone
from news.models import Post
from subscriptions.models import Subscription


@shared_task
def msg_new_post(pk):
    post = Post.objects.get(pk=pk)
    categories = post.post_category.all()
    heading = post.heading
    content = post.content()
    subscribers_emails = []

    for category in categories:
        subscribers = category.subscribers.all()
        subscribers_emails += [subscriber.email for subscriber in subscribers]

    html_content = render_to_string(
        'new_post_email.html',
        {
            'text': content,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=f'{heading} from celery',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers_emails
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def weekly_post():
    today = timezone.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(time_in__gte=last_week)
    categories = set(posts.values_list('post_category', flat=True))
    subscribers = set(Subscription.objects.filter(category__in=categories).values_list('user__email', flat=True))

    html_content = render_to_string(
        'weeky_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }

    )
    msg = EmailMultiAlternatives(
        subject='Публикации за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()