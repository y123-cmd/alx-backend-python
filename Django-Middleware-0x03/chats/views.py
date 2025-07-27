from django.shortcuts import render
from .serializers import ConversationSerializer, MessageSerializer
from .models import Message, Conversation
from rest_framework import viewsets, status, filters

# authentication & Permisions api views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .permissions import IsOwnerOfConversation, IsOwnerOfMessage, IsParticipantOfConversation


# viewset to perform CRUD operations

class ConversationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    # queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def get_queryset(self):
        # Only return conversations the user is a participant in
        return Conversation.objects.filter(participants=self.request.user)

    def get(self, request):
        return Response({'message': 'Hello authenticated user'}, status=status.HTTP_200_OK)


class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,
                          IsOwnerOfMessage, IsParticipantOfConversation]
    serializer_class = MessageSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['sent_at']

    def get_queryset(self):
        conversation_id = self.request.query_params.get('conversation_id')
        if conversation_id:
            return Message.objects.filter(
                conversation_id=conversation_id,
                conversation__participants=self.request.user
            )
        return Message.objects.filter(conversation__participants=self.request.user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user not in instance.conversation.participants.all():
            return Response(
                {"detail": "You are not authorized to view this message."},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
