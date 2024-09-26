from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from likes.model import Likes
from likes.serializers import LikeSerializer

class LikesList(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
        serializer_class = LikeSerializer
        queryset = Like.objects.all()

        def perform_create(self, Serializer)
    ]