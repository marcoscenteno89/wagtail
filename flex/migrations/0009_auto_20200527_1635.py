# Generated by Django 3.0.5 on 2020-05-27 16:35

from django.db import migrations
import flex.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0008_auto_20200527_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='body',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('margin', wagtail.core.blocks.CharBlock(help_text='Add Custom Margin', required=False)), ('padding', wagtail.core.blocks.CharBlock(help_text='Add Custom Padding', required=False)), ('background_color', wagtail.core.blocks.CharBlock(help_text='Add Custom Background', required=False)), ('element_classes', wagtail.core.blocks.CharBlock(help_text='Add Custom Classes', required=False)), ('element_id', wagtail.core.blocks.CharBlock(help_text='Add Custom Element ID', required=False)), ('background_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='add additional text', required=True))])), ('full_richtext', flex.blocks.RichtextBlock()), ('carousel', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('text', wagtail.core.blocks.TextBlock(max_length=300, required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='Custom Url', required=False))])))])), ('button', wagtail.core.blocks.StructBlock([('margin', wagtail.core.blocks.CharBlock(help_text='Add Custom Margin', required=False)), ('padding', wagtail.core.blocks.CharBlock(help_text='Add Custom Padding', required=False)), ('background_color', wagtail.core.blocks.CharBlock(help_text='Add Custom Background', required=False)), ('element_classes', wagtail.core.blocks.CharBlock(help_text='Add Custom Classes', required=False)), ('element_id', wagtail.core.blocks.CharBlock(help_text='Add Custom Element ID', required=False)), ('background_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(blank=True, max_length=500)), ('label', wagtail.core.blocks.CharBlock(help_text='Label', required=False))]))], blank=True, null=True),
        ),
    ]
