# Generated by Django 4.0.1 on 2022-02-10 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_category_alter_newsstory_options_newsstory_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
