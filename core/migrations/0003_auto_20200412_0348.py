# Generated by Django 3.0.5 on 2020-04-12 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200412_0319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='user',
            new_name='author',
        ),
    ]
