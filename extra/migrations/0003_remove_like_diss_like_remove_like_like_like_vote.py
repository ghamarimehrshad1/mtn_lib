# Generated by Django 4.0.4 on 2022-06-16 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0002_rename_vote_like_diss_like_like_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='diss_like',
        ),
        migrations.RemoveField(
            model_name='like',
            name='like',
        ),
        migrations.AddField(
            model_name='like',
            name='vote',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
