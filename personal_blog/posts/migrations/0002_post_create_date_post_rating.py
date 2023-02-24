# Generated by Django 4.1.7 on 2023-02-24 11:46

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(blank=True, default=django.utils.datetime_safe.datetime.now),
        ),
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
