# Generated by Django 3.0.5 on 2020-05-26 21:05

from django.db import migrations
import flex.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0004_auto_20200526_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='body',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='add additional text', required=True))])), ('full_richtext', flex.blocks.RichtextBlock()), ('simple_richtext', flex.blocks.SimpleRichtextBlock()), ('carousel', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('text', wagtail.core.blocks.TextBlock(max_length=300, required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='Custom Url', required=False))])))])), ('button', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(help_text='Label', required=False))]))], blank=True, null=True),
        ),
    ]
