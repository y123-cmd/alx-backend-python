import django_filters
from .models import Message

class MessageFilter(django_filters.FilterSet):
    sender = django_filters.CharFilter(field_name='sender__username', lookup_expr='iexact')
    participant = django_filters.CharFilter(method='filter_by_participant')
    sent_after = django_filters.DateTimeFilter(field_name='sent_at', lookup_expr='gte')
    sent_before = django_filters.DateTimeFilter(field_name='sent_at', lookup_expr='lte')

    class Meta:
        model = Message
        fields = ['sender', 'participant', 'sent_after', 'sent_before']

    def filter_by_participant(self, queryset, name, value):
        return queryset.filter(conversation__participants__username__iexact=value)
