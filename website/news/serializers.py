from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

# import Category model

from .models import Category, News, Comment

# Membuat class Serializers untuk API endpoint "Get List of Categories"
class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name',)

# Membuat class Serializers untuk API endpoint "Get Detail of Category"

class CategoryDetailSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name','created_at',)


#Membuat class UserSerializer yang akan berelasi ke NewsSerializer
class UserSerializier(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name',)

# Membuat class CommentListSerializer yang akan berelasi ke NewsSerializer
class CommentListSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','name','content','created_at',)

# Membuat class CommentFormSerializer yang akan berelasi ke NewsSerializer
class CommentFormSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('name','email','content',)


# Membuat class NewsListSerializer untuk API endpoint "Get List of News"

class NewsListSerializer(ModelSerializer):
    user = UserSerializier(read_only=True) # relasi ke modul/tabel user
    category = CategoryListSerializer(many=True, read_only=True) # relasi ke modul/tabel category

    class Meta:
        model = News
        fields = ('id','title','excerpt','user','category','published_at')

# Membuat class NewsDetailSerializer untuk API endpoint "Get Detail of News"
class NewsDetailSerializer(ModelSerializer):
    user = UserSerializier(read_only=True)
    category = CategoryListSerializer(many=True, read_only=True) # relasi ke modul/tabel category
    comment = CommentListSerializer(many=True, read_only=True, source='comment_set') # relasi ke modul/tabel comment

    class Meta:
        model = News
        fields = ('id','title','excerpt','content','cover','published_at','user','category','comment')




