# Generated by Django 3.2 on 2023-06-17 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item_list',
            old_name='item2',
            new_name='item3',
        ),
    ]
