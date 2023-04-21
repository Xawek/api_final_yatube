from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        help_text='Опишите смысл, если есть.'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        verbose_name=('Автор'),
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        verbose_name=('Группы'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        help_text=(
            'Необязательно'
        )
    )
    image = models.ImageField(
        upload_to='posts/',
        blank=True,
        null=True,
        help_text='Необязательно'
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name=('Комментарий'),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text='Необязательно',
        related_name='comments',
    )
    author = models.ForeignKey(
        User,
        verbose_name=('Автор'),
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField()
    created = models.DateTimeField(
        auto_now_add=True,
    )


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )
