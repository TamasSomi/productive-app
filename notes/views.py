from rest_framework import generics, permissions
from productive_app.permissions import IsOwnerOrReadOnly
from .models import Note
from .serializers import NoteSerializer, NoteDetailSerializer
from rest_framework.exceptions import PermissionDenied


class NoteList(generics.ListCreateAPIView):
    """
    API view for listing and creating Note instances.
    """
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Note.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = NoteDetailSerializer
    queryset = Note.objects.all()

    # only the owner can see the note
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(owner=user)
