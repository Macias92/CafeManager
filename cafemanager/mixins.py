from django.utils.translation import gettext as _
from django.contrib.admin.models import ADDITION, CHANGE, ContentType, DELETION, LogEntry


class CustomLoggingMixin:
    """Returns logs of logged User"""
    def _visitor_ip_address(self):
        """Returns ip address of logged user"""
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip

    def _visitor_agent(self):
        """Returns the browser agent"""
        return self.request.META['HTTP_USER_AGENT']

    def log(self, operation, instance):
        """Creates a log"""
        if operation == ADDITION:
            action_message = _('Created')
        if operation == CHANGE:
            action_message = _('Updated')
        if operation == DELETION:
            action_message = _('Deleted')

        message = {
            'action': action_message,
            'instance': str(instance),
            'ip': self._visitor_ip_address(),
            'agent': self._visitor_agent(),
        }
        LogEntry.objects.log_action(
            user_id=self.request.user.id,
            content_type_id=ContentType.objects.get_for_model(instance).pk,
            object_id=instance.pk,
            object_repr=str(instance),
            action_flag=operation,
            change_message=message
        )

    def log_create(self, serializer):
        self.log(operation=ADDITION, instance=serializer.instance)


class CustomLoggingViewSetMixin(CustomLoggingMixin):
    def perform_create(self, serializer):
        super().perform_create(serializer)
        self.log_create(serializer)

    def perform_udpate(self, serializer):
        super().perform_update(serializer)
        self.log_update(serializer)

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        self.log_destroy(instance)
