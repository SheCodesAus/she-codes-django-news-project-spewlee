# Generated by Django 4.0.1 on 2022-02-18 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_alter_newsstory_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsstory',
            name='likes',
        ),
    ]
