# Generated by Django 3.0.5 on 2020-05-22 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_menu_menuitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='open_in_new_tab',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
