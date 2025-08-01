from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory
from django.db.models.signals import post_delete
from django.contrib.auth.models import User

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:  
        try:
            old_message = Message.objects.get(pk=instance.pk)
            if old_message.content != instance.content:
                
                MessageHistory.objects.create(
                    message=instance,
                    old_content=old_message.content
                )
                
                instance.edited = True
        except Message.DoesNotExist:
            pass 

@receiver(post_delete, sender=User)
def delete_related_user_data(sender, instance, **kwargs):
    Message.objects.filter(user=instance).delete()
    Notification.objects.filter(user=instance).delete()
    MessageHistory.objects.filter(message__user=instance).delete()
