from rest_framework import serializers
from clients.models import Profile


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'
