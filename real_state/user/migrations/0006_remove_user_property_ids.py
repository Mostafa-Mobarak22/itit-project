# Generated by Django 5.1.1 on 2024-10-05 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_property_ids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='property_ids',
        ),
    ]
