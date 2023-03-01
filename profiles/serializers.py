from rest_framework import serializers

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
    class Meta:
        model = Profiles
        fields = '__all__'

