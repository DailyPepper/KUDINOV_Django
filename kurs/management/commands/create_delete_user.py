from django.core.management.base import BaseCommand
from KUDINOV.models import Customer


class Command(BaseCommand):
    help = 'Create or delete users'

    def add_arguments(self, parser):
        parser.add_argument('action', choices=['create', 'delete'], help='Action to perform')
        parser.add_argument('username', help='Username')

    def handle(self, *args, **options):
        action = options['action']
        username = options['username']

        if action == 'create':
            user = Customer.objects.create(username=username)
            self.stdout.write(self.style.SUCCESS(f'Successfully created user: {user.username}'))
        elif action == 'delete':
            try:
                user = Customer.objects.get(username=username)
                user.delete()
                self.stdout.write(self.style.SUCCESS(f'Successfully deleted user: {username}'))
            except Customer.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'User with username {username} does not exist'))
