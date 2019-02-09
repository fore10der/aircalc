from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in

@receiver(user_logged_in)
def group_redirect(sender):
    print(sender)