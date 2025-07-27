from rest_framework import permissions


class IsOwnerOfConversation(permissions.BasePermission):
    """
    Permission to ensure the user is part of the conversation.
    """

    def has_object_permission(self, request, view, obj):
        # Assumes the Conversation model has a participants ManyToMany field
        return request.user in obj.participants.all()


class IsOwnerOfMessage(permissions.BasePermission):
    """
    Permission to ensure the user owns the message (either as sender or recipient).
    """

    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user or obj.recipient == request.user


class IsParticipantOfConversation(permissions.BasePermission):
    """
    Allows access only to participants of the conversation.
    Explicitly checks for safe and unsafe methods.
    """

    def has_permission(self, request, view):
        # Ensure the user is authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user

        if hasattr(obj, 'participants'):
            # Conversation instance
            is_participant = user in obj.participants.all()
        elif hasattr(obj, 'conversation'):
            # Message instance
            is_participant = user in obj.conversation.participants.all()
        else:
            return False

        # Explicitly handle common HTTP methods for clarity
        if request.method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
            return is_participant

        return False
