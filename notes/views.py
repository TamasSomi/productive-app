from rest_framework import generics, permissions
from productive_app.permissions import IsOwnerOrReadOnly
from .models import Note
from .serializers import NoteSerializer, NoteDetailSerializer


class NoteList(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Note.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = NoteDetailSerializer
    queryset = Note.objects.all()
