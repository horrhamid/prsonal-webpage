# Generated by Django 3.0 on 2019-12-15 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='is_ative',
            field=models.BooleanField(default=False),
        ),
    ]
