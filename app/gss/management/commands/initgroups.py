from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'Initialize user groups'

    def handle(self, *args, **kwargs):
        Group.objects.get_or_create(name='can_input')
        Group.objects.get_or_create(name='can_report')