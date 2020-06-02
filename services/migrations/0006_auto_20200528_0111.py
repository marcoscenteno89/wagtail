# Generated by Django 3.0.5 on 2020-05-28 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20200528_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promotion',
            name='page_ptr',
        ),
        migrations.AddField(
            model_name='promotion',
            name='id',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='promotion',
            name='title',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]