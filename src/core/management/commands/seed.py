from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from src.core.models import Customer


class Command(BaseCommand):
    help = 'Seed project data'

    def handle(self, *args, **options):
        Customer.objects.get_or_create(
            name='Customer A', phone='12345678911'
        )
        Customer.objects.get_or_create(
            name='Customer B', phone='12345678912'
        )
        Customer.objects.get_or_create(
            name='Customer B', phone='12345678913'
        )
        Customer.objects.get_or_create(
            name='Customer B', phone='12345678914'
        )
        Customer.objects.get_or_create(
            name='Customer B', phone='12345678915'
        )
        Customer.objects.get_or_create(
            name='Customer B', phone='12345678916'
        )
        Customer.objects.get_or_create(
            name='Customer B', phone='12345678917'
        )
        Customer.objects.get_or_create(
            name='Customer B', phone='12345678918'
        )
        Customer.objects.get_or_create(
            name='Customer B', phone='12345678919'
        )
        Customer.objects.get_or_create(
            name='Customer B', phone='12345678910'
        )
        Customer.objects.get_or_create(
            name='Customer B', phone='12345678920'
        )
        Customer.objects.get_or_create(
            name='Customer B', phone='12345678921'
        )

        self.stdout.write(self.style.SUCCESS('Seeding has completed successfully!'))
