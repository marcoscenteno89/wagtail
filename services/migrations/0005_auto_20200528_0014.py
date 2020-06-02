# Generated by Django 3.0.5 on 2020-05-28 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('services', '0004_promotion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='promotion',
            options={'verbose_name': 'Promotion', 'verbose_name_plural': 'Promotions'},
        ),
        migrations.RemoveField(
            model_name='promotion',
            name='id',
        ),
        migrations.RemoveField(
            model_name='promotion',
            name='title',
        ),
        migrations.AddField(
            model_name='promotion',
            name='page_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page'),
            preserve_default=False,
        ),
    ]