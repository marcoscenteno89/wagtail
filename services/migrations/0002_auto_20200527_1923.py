# Generated by Django 3.0.5 on 2020-05-27 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='company',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='service_type',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]