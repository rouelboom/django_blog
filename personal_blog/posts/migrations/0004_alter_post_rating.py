# Generated by Django 4.1.7 on 2023-02-24 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
