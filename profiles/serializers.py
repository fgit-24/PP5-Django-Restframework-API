from rest_framework import serializers
from .models import Profile
from PIL import Image as PilImage
import io

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def validate_image(self, value):
        try:
            img = PilImage.open(value)
            if img.format not in ['JPEG', 'JPG']:
                raise serializers.ValidationError("Only JPG images are allowed.")
        except Exception as e:
            raise serializers.ValidationError("Invalid image file. Error: " + str(e))
        return value

    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'created_at',
            'updated_at',
            'username',
            'bio',
            'image',
            'is_owner',
        ]