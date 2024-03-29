from rest_framework import serializers
from tasks.models import Task
from django.core.exceptions import ValidationError
from django.utils import timezone


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    notes_count = serializers.ReadOnlyField()

    def validate_deadline(self, value):
        """
        Validate that the deadline is not in the past.
        """
        if value and value < timezone.now():
            raise ValidationError("Deadline cannot be in the past.")
        return value

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 20:
            raise serializers.ValidationError(
                'Image size larger than 20MB'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Task
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'deadline',
            'image_filter', 'notes_count'
        ]
