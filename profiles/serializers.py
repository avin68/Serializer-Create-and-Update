from rest_framework import serializers
import re
from rest_framework.exceptions import ValidationError

from posts.models import Posts
from posts.serializers import PostSerializer
from profiles.models import Profiles

'''
class ProfileSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=70)

    def create(self, validated_data):
        return Profiles.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.phone_number = validated_data.get('phone_number')
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.save()
        return instance
'''


class ProfileSerializer(serializers.ModelSerializer):
    # posts = PostSerializer(many=True, read_only=True)
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    post = PostSerializer(write_only=True)

    class Meta:
        model = Profiles
        fields = '__all__'

    def validate_phone_number(self, value):
        phone_number_pattern = re.compile('^09\d{9}')
        if phone_number_pattern.match(value):
            return value
        raise ValidationError('ERROR!!!...')

    def create(self, validated_data):
        post = validated_data.pop('post')
        profile = Profiles.objects.create(**validated_data)
        my_post = Posts.objects.create(**post, author=profile)
        return profile
