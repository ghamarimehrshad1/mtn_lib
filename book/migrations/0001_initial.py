# Generated by Django 4.0.4 on 2022-06-06 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounting', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('cover', models.ImageField(blank=True, default='cover_book/default.png', upload_to='cover_book')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('traslator', models.CharField(max_length=100)),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('book', models.ManyToManyField(to='book.book')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounting.customuser')),
            ],
        ),
    ]
