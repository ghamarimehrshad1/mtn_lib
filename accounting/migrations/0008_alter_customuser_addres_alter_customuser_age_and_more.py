# Generated by Django 4.0.4 on 2022-06-30 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0007_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='addres',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='national_code',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]
