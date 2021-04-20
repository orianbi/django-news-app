from django.db import models
from django.contrib.auth.models import User
# import class untuk menggenerate token user
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

#Model untuk tabel category

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)

    #set nama tabel
    class Meta:
        db_table = 'category'
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name

# Membuat Custom Manager untuk NewsModel
class NewsManager(models.Manager):
    # Menambah method untuk memfilter news yang hanya berstatus 'published'
    def is_published(self):
        return super().get_queryset().filter(status=News.NewsStatus.published)

#Model untuk tabel news
class News(models.Model):
    class NewsStatus(models.IntegerChoices):
        draft = 1
        published = 2

    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='images')
    content = models.TextField()
    excerpt = models.TextField()
    status = models.IntegerField(choices=NewsStatus.choices)
    published_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #set relasi ke tabel user dan category
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    # Menambahkan NewsManager
    objects = NewsManager()

    #set nama tabel 
    class Meta:
        db_table = 'news'
        verbose_name_plural = "News"

    def __str__(self):
        return self.title


#Model untuk tabel comment

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #set relasi ke tabel news

    news = models.ForeignKey(News, on_delete=models.CASCADE)

    #set nama tabel

    class Meta:
        db_table = 'comment'
        verbose_name_plural = "Comment"

# Method untuk menggenerate token secara otomatis untuk Otentikasi Rest API ketika user dibuat
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)

def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)