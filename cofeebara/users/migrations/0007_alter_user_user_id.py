# Generated by Django 5.1.3 on 2025-03-25 05:23

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_user_id_alter_user_user_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('93fd95fc-d2df-4e46-a422-7671409fde8d'), primary_key=True, serialize=False, unique=True),
        ),
    ]
