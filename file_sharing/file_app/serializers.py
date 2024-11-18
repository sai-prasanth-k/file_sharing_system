from rest_framework import serializers
from .models import User, File

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'is_ops_user']

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['file']