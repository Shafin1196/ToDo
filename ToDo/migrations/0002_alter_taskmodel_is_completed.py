# Generated by Django 5.1.2 on 2024-12-06 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
