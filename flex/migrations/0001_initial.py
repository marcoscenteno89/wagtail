# Generated by Django 3.0.5 on 2020-05-22 16:01

from django.db import migrations, models
import django.db.models.deletion
import flex.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='add additional text', required=True))])), ('full_richtext', flex.blocks.RichtextBlock()), ('simple_richtext', flex.blocks.SimpleRichtextBlock()), ('carousel', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('text', wagtail.core.blocks.TextBlock(max_length=300, required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='this is a test', required=False))])))])), ('button', wagtail.core.blocks.StructBlock([('button_page', wagtail.core.blocks.PageChooserBlock(help_text='If selected, this url will be used', required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If selected, this page will be used', required=False))]))], blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Flex Page',
                'verbose_name_plural': 'Flex Pages',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, help_text='Facebook', null=True)),
                ('twitter', models.URLField(blank=True, help_text='Twitter', null=True)),
                ('youtube', models.URLField(blank=True, help_text='Youtube', null=True)),
                ('google', models.URLField(blank=True, help_text='google', null=True)),
                ('pinterest', models.URLField(blank=True, help_text='pinterest', null=True)),
                ('linkedin', models.URLField(blank=True, help_text='linkedin', null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]