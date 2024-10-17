from django.db import models
from django.contrib.auth import get_user_model  # Use this for better compatibility
import uuid

# Get the user model
User = get_user_model()

class ChatRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    members = models.ManyToManyField(User, related_name="chat_rooms", blank=True)

    def __str__(self):
        return f"ChatRoom {self.id} with members: {', '.join([member.username for member in self.members.all()])}"

class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages', null=True, blank=True)  # Allow null for receiver

    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username if self.receiver else 'None'} in {self.room.id}: {self.content[:20]}..."