from rest_framework import serializers

from blog.models import Profile, Category, Post, Comment
from gallery.serializers import GallerySerializer


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    text = serializers.SlugRelatedField(slug_field='text', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    gallery = GallerySerializer()
    comment = CommentSerializer()

    class Meta:
        model = Post
        fields = '__all__'


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
