from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates test users for the chat application'

    def handle(self, *args, **options):
        # Create test users
        test_users = [
            {'username': 'alice', 'password': 'password123', 'email': 'alice@example.com'},
            {'username': 'bob', 'password': 'password123', 'email': 'bob@example.com'},
            {'username': 'charlie', 'password': 'password123', 'email': 'charlie@example.com'},
            {'username': 'diana', 'password': 'password123', 'email': 'diana@example.com'},
        ]
        
        created_count = 0
        for user_data in test_users:
            if not User.objects.filter(username=user_data['username']).exists():
                user = User.objects.create_user(
                    username=user_data['username'],
                    email=user_data['email'],
                    password=user_data['password']
                )
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created user: {user.username}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'User {user_data["username"]} already exists')
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} new users')
        ) 