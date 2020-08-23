from django.core.management.base import BaseCommand
from apps.user.models import Account

class Command(BaseCommand):
    def handle(self, *args, **options):
        if Account.objects.count() == 0:
            username = "admin@example.com"
            email = "admin@example.com"
            password = 'admin'
            print('Creating account for %s (%s)' % (username, email))
            admin = Account.objects.create_superuser(email=email, username=username, password=password)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')