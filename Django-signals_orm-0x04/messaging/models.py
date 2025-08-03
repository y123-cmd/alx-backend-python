from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    parent_message = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='replies',
        on_delete=models.CASCADE
    )
    read = models.BooleanField(default=False)  

    objects = models.Manager()  
    unread = None  

    def save(self, *args, **kwargs):
        editor = kwargs.pop('editor', None)  
        if self.pk:
            old = Message.objects.get(pk=self.pk)
            if old.content != self.content:
                self.edited = True
                MessageHistory.objects.create(
                    message=self,
                    old_content=old.content,
                    edited_by=editor
                )
        super().save(*args, **kwargs)

    def get_all_replies(self):
        replies = []
        for reply in self.replies.all():
            replies.append(reply)
            replies.extend(reply.get_all_replies())
        return replies

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Notification for {self.user} - Message ID: {self.message.id}'

class MessageHistory(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='history')
    old_content = models.TextField()
    edited_at = models.DateTimeField(auto_now_add=True)
    edited_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Edit by {self.edited_by} on message ID {self.message.id}'


class UnreadMessagesManager(models.Manager):
    def for_user(self, user):
        return self.get_queryset().filter(receiver=user, read=False).only('id', 'sender', 'content', 'timestamp')


Message.unread = UnreadMessagesManager()

