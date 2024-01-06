from django.core.management.base import BaseCommand
from KUDINOV.models import Customer

class Command(BaseCommand):
    help = 'Выводит список всех клиентов'

    def handle(self, *args, **kwargs):
        customers = Customer.objects.all()
        for customer in customers:
            self.stdout.write(self.style.SUCCESS(f'Customer: {customer.first_name} {customer.last_name}, Email: {customer.email}'))
