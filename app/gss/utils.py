from django.contrib.auth.decorators import user_passes_test
from gss.settings.base import LOGIN_REDIRECT_URL
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def group_required(*group_names):
   """Requires user membership in at least one of the groups passed in."""

   def in_groups(u):
       if u.is_authenticated:
           if u.groups.filter(name__in=group_names).exists() | u.is_superuser:
               return True
       return False
   return user_passes_test(in_groups, login_url='error', redirect_field_name=None)

def anonymous_required(function=None, redirect_url=None):
    if not redirect_url:
        redirect_url = LOGIN_REDIRECT_URL

    actual_decorator = user_passes_test(
        lambda u: u.is_anonymous,
        login_url=redirect_url
    )

    if function:
        return actual_decorator(function)
    return actual_decorator

def notificate(user_id, type, info):
    layer = get_channel_layer()
    async_to_sync(layer.group_send)(f'group-{user_id}', {
        'type': type,
        'content': info
    })