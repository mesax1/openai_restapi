# Generated by Django 4.1.7 on 2023-03-14 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gptapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatgpt',
            name='stream',
        ),
    ]
