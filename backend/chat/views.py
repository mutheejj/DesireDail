from django.db.models import Q, Max, Count
from django.db.models.functions import Coalesce
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound, PermissionDenied
from django.shortcuts import get_object_or_404
from .models import ChatRoom, Message
from .serializers import MessageSerializer, FriendsSerializer
from user.serializers import UserProfileSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetOrCreateChatroom(request, username):
    if request.user.username == username:
        return Response({"message": "Cannot chat with yourself."}, status=status.HTTP_406_NOT_ACCEPTABLE)

    other_user = get_object_or_404(User, username=username)

    # Check if a chatroom with the other user already exists
    chatroom = ChatRoom.objects.filter(members=request.user).filter(members=other_user).first()
    if chatroom:
        members_data = UserProfileSerializer(chatroom.members.all(), many=True, context={'request': request}).data
        return Response({'chatroom': str(chatroom.id), 'members': members_data})

    # Create a new chatroom if none exists
    chatroom = ChatRoom.objects.create()
    chatroom.members.add(other_user, request.user)
    members_data = UserProfileSerializer(chatroom.members.all(), many=True, context={'request': request}).data
    return Response({'chatroom': str(chatroom.id), 'members': members_data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ChatView(request, room_id):
    chatroom = get_object_or_404(ChatRoom, id=room_id)
    
    # Check if the user is a member of the chatroom
    if request.user not in chatroom.members.all():
        raise PermissionDenied('You don\'t have permission to access this chat room')
    
    # Mark messages as read
    Message.objects.filter(receiver=request.user, room=chatroom, is_read=False).update(is_read=True)
    messages = Message.objects.filter(room=chatroom)
    serializer = MessageSerializer(messages, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def RemoveFriend(request, username):
    user = request.user
    friend = get_object_or_404(user.friends, username=username)

    # Find the chatroom with the friend
    friend_chatroom = user.chat_rooms.filter(members=friend).first()

    if friend_chatroom:
        Message.objects.filter(room=friend_chatroom).delete()
        friend_chatroom.delete()
        user.friends.remove(friend)
        return Response({'message': 'Successfully Deleted!'})

    return Response({'message': 'Error Deleting!'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ListFriends(request):
    user = request.user
    serializer = FriendsSerializer(user)
    return Response(serializer.data)

class ListFriendsProfile(generics.ListAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        return current_user.friends.annotate(
            last_message_date=Coalesce(
                Max('sent_messages__created_at', filter=Q(sent_messages__receiver=current_user)),
                Max('received_messages__created_at', filter=Q(received_messages__sender=current_user))
            )
        ).order_by('-last_message_date')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def MarkAsRead(request):
    msg_id = request.data.get('msg_id')
    try:
        message = Message.objects.get(id=msg_id)
        message.is_read = True
        message.save ()
        return Response({'status': 'success', 'message': 'Message marked as read'}, status=status.HTTP_200_OK)
    except Message.DoesNotExist:
        return Response({'status': 'error', 'message': 'Message not found'}, status=status.HTTP_404_NOT_FOUND)