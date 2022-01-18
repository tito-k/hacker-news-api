from rest_framework import serializers

from .models import Base


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = ['id', 'type', 'by', 'time', 'kids']
        read_only_fields = ['id']


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = ['id', 'type', 'by', 'time', 'kids', 'text', 'url', 'title']
        read_only_fields = ['id']


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = ['id', 'type', 'by', 'time', 'kids',
                  'descendants', 'score', 'title', 'url']
        read_only_fields = ['id']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = ['id', 'type', 'by', 'time', 'kids',
                  'parent', 'text']
        read_only_fields = ['id']


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = ['id', 'type', 'by', 'time', 'kids',
                  'parts', 'descendants', 'score', 'title', 'text']
        read_only_fields = ['id']


class PollOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = ['id', 'type', 'by', 'time', 'kids',
                  'parent', 'score']
        read_only_fields = ['id']
