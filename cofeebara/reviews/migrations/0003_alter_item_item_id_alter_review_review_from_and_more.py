# Generated by Django 5.1.3 on 2025-03-24 02:03

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_item_alter_review_review_id_and_more'),
        ('users', '0005_alter_user_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_id',
            field=models.UUIDField(default=uuid.UUID('d51e720e-ba76-4030-9fde-2e331d1ebd89'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='users.user'),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_id',
            field=models.UUIDField(default=uuid.UUID('10929f7a-7160-40ec-abaa-70a8958a6ab0'), primary_key=True, serialize=False, unique=True),
        ),
    ]
