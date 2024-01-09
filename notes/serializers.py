from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Note model
    Adds three extra fields when returning a list of Note instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Note
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'task', 'created_at', 'updated_at', 'content'
        ]


class NoteDetailSerializer(NoteSerializer):
    """
    Serializer for the Note model used in Detail view
    """
    task = serializers.ReadOnlyField(source='task.id')
