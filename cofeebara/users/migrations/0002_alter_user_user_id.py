# Generated by Django 5.1.3 on 2025-03-18 06:46

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('71c71d14-ff2d-4bce-a03d-6b9332da4cad'), primary_key=True, serialize=False, unique=True),
        ),
    ]
