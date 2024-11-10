from rest_framework import serializers
from pathlib import Path
from taggit.serializers import TagListSerializerField, TaggitSerializer
from .models import Post
from likes.models import Like
from PIL import Image as PilImage

class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    """
    Serializer for the Post model, checks for owner of the post.
    Comment and download counts.
    Has tagging functionality, and image size validation.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    comments_count = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
        

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, post=obj).first()
            return like.id if like else None
        return None

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_comments_count(self, obj):
        return obj.comments.count()

    class Meta:
        model = Post
        fields = [
            'id',
            'owner',
            'created_at',
            'updated_at',
            'title',
            'content',
            'image',
            'is_owner',
            'profile_id',
            'comments_count',
            'like_id',
            'likes_count',
        ]
