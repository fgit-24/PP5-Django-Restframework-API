from rest_framework import generics, permissions
from .models import Album
from .serializers import AlbumSerializer


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    If you own it, manage your album: view, update, or delete.
    """
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Album.objects.filter(owner=user)


class AlbumList(generics.ListCreateAPIView):
    """
    Returns a list of all albums.
    An authenticated user can create an album.
    nly the album owner can view their own albums.
    """
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Album.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
