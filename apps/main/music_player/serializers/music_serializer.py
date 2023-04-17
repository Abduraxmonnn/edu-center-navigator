# Rest-Framework
from rest_framework.serializers import ModelSerializer

# Project
from apps.main.music_player.models import Music


class MusicSerializer(ModelSerializer):
    class Meta:
        model = Music
        fields = [
            'id',
            'name',
            'file',
            'size_type',
            'size',
            'format_file',
        ]
