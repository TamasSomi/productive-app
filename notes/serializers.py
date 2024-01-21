from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Note model.

    This serializer extends the basic functionality of the Note model
    by adding extra fields for improved representation in API responses.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

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
