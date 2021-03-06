# Generated by Django 4.0.4 on 2022-06-06 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
        ('author', '0001_initial'),
        ('accounting', '0002_initial'),
        ('extra', '0001_initial'),
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extra.publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='author.author'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(to='extra.category'),
        ),
        migrations.AddField(
            model_name='book',
            name='loan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.loan'),
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.customuser'),
        ),
    ]
