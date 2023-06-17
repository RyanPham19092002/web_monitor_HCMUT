# Generated by Django 3.2 on 2023-06-17 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lis', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Item_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item1', models.CharField(max_length=300)),
                ('item2', models.CharField(max_length=300)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetups.list')),
            ],
        ),
    ]
