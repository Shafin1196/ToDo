# Generated by Django 5.1.2 on 2024-12-06 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=100)),
                ('taskDescription', models.CharField(max_length=100)),
                ('is_completed', models.BooleanField()),
            ],
        ),
    ]
