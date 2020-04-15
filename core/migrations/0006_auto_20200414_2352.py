# Generated by Django 3.0.5 on 2020-04-14 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_tweet_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextPair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=280)),
                ('isHash', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='tweet',
            name='parsed',
            field=models.ManyToManyField(to='core.TextPair'),
        ),
    ]
