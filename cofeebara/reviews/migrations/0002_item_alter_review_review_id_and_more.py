# Generated by Django 5.1.3 on 2025-03-13 02:51

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('item_id', models.UUIDField(default=uuid.UUID('23f662a3-4e3f-43c0-aa41-61b8bfc5a029'), primary_key=True, serialize=False, unique=True)),
                ('item_name', models.CharField(max_length=64)),
                ('item_feature', models.TextField(max_length=512)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='review',
            name='review_id',
            field=models.UUIDField(default=uuid.UUID('b96a6e38-8961-4b79-87ec-f8175344001b'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_about',
            field=models.ForeignKey(db_column='item_id', on_delete=django.db.models.deletion.CASCADE, to='reviews.item'),
        ),
        migrations.DeleteModel(
            name='Items',
        ),
    ]
