# Generated by Django 5.2 on 2025-04-04 14:20

from django.db import migrations
from django.contrib.auth import get_user_model
import os

# Define the user credentials
USERNAME = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'DeveloperX')
EMAIL = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com') # Needed if creating
PASSWORD = 'ResetMeNow123!' # TEMPORARY - Change immediately after login

def create_or_reset_superuser(apps, schema_editor):
    User = get_user_model()
    try:
        # Try to find the existing user
        user = User.objects.get(username=USERNAME)
        user.set_password(PASSWORD)
        user.save()
        print(f'\nPassword for existing user {USERNAME} has been reset.')
    except User.DoesNotExist:
        # User not found, so create them
        print(f'\nUser {USERNAME} not found. Creating user...')
        User.objects.create_superuser(
            username=USERNAME,
            email=EMAIL,
            password=PASSWORD
        )
        print(f'Superuser {USERNAME} created with temporary password.')

class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_create_superuser'), # Depends on the previous attempt
    ]

    operations = [
        # Rename the function being called if you changed its name
        migrations.RunPython(create_or_reset_superuser),
    ]
