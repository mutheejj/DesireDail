from rest_framework import serializers
from .models import Message, ChatRoom
from user.models import User

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'content', 'sender', 'receiver', 'room', 'created_at', 'is_read']  # Explicitly list fields

class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id', 'members']  # Explicitly list fields

class FriendsSerializer(serializers.ModelSerializer):
    friends = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'friends']

    def get_friends(self, obj):
        return obj.friends.values_list('username', flat=True)