# Generated by Django 5.1.3 on 2025-03-13 02:36

import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('item_id', models.UUIDField(default=uuid.UUID('8adafe51-0f25-4bf7-8d3e-5fa103aa51da'), primary_key=True, serialize=False, unique=True)),
                ('item_name', models.CharField(max_length=64)),
                ('item_feature', models.TextField(max_length=512)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('review_id', models.UUIDField(default=uuid.UUID('e4c6b33f-86dd-4f12-b2a1-91cad1e40c8c'), primary_key=True, serialize=False, unique=True)),
                ('review_text', models.TextField(max_length=512)),
                ('review_rating', models.IntegerField(choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('review_about', models.ForeignKey(db_column='item_id', on_delete=django.db.models.deletion.CASCADE, to='reviews.items')),
                ('review_from', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
