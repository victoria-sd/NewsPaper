from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    user_rate = models.IntegerField(default=0)
    author = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        # суммарный рейтинг всех комментариев к статьям
        sum_rating = self.post_set.aggregate(post_rating=Sum('post_rate'))
        result_sum_rating = 0
        result_sum_rating += sum_rating.get('post_rating')

        # суммарный рейтинг всех комментариев самого автора
        sum_comment_rating = self.author.comment_set.aggregate(comment_rating=Sum('comment_rate'))
        result_sum_comment_rating = 0
        result_sum_comment_rating += sum_comment_rating.get('comment_rating')

        # суммарный рейтинг каждой статьи автора умноженный на 3
        self.user_rate = result_sum_rating * 3 + result_sum_comment_rating
        self.save()


class Category(models.Model):
    name_category = models.CharField(max_length=64, unique=True)


class Post(models.Model):
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_category = models.ManyToManyField(Category, through='PostCategory')

    article = 'A'
    news = 'N'

    POSITIONS = [
        (article, "Статья"),
        (news, "Новость"),
    ]

    category = models.CharField(max_length=1, choices=POSITIONS, default=news)
    time_in = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=64) #заголовок
    content = models.TextField() # текст статьи/новости
    post_rate = models.IntegerField(default=0)  # рейтинг

    def like(self):
        self.post_rate += 1
        self.save()

    def dislike(self):
        self.post_rate -= 1
        self.save()

    def preview(self):
        return self.content[0:124] + "..."

    def __str__(self):
        return f'{self.heading.title()}: {self.content[:50]}'


class PostCategory(models.Model):
    post_through = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_through = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=64)
    time_in = models.DateTimeField(auto_now_add=True)
    comment_rate = models.IntegerField(default=0)

    def like(self):
        self.comment_rate += 1
        self.save()

    def dislike(self):
        self.comment_rate -= 1
        self.save()


