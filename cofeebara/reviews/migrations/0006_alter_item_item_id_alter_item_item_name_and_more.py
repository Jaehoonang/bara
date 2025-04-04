# Generated by Django 5.1.3 on 2025-04-01 02:21

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_remove_review_review_from_alter_item_item_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_id',
            field=models.UUIDField(default=uuid.UUID('13506a2b-440a-4fb9-8357-aa6cb888d42a'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_id',
            field=models.UUIDField(default=uuid.UUID('001dafdb-f7c5-437d-8dab-aa83e9ac2860'), primary_key=True, serialize=False, unique=True),
        ),
    ]
