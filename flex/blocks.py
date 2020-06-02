from wagtail.core import blocks
from django.db import models
# from wagtail.core.models import Orderable
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from modelcluster.fields import ParentalKey
# from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField


class BlockSettings(blocks.StructBlock):
    margin = blocks.CharBlock(required=False, help_text='Add Custom Margin',)
    padding = blocks.CharBlock(required=False, help_text='Add Custom Padding')
    background_color = blocks.CharBlock(required=False, help_text='Add Custom Background')
    element_classes = blocks.CharBlock(required=False, help_text='Add Custom Classes')
    element_id = blocks.CharBlock(required=False, help_text='Add Custom Element ID')
    background_image = ImageChooserBlock(required=False)

    MultiFieldPanel([
        FieldPanel('margin'),
        FieldPanel('padding'),
        FieldPanel('background_color'),
        FieldPanel('element_classes'),
        FieldPanel('element_id'),
        FieldPanel('background_image'),
    ], heading='Custom Settings', classname='collapsible collapsed'),


class TitleAndTextBlock(BlockSettings):
    title = blocks.CharBlock(required=True, help_text='Add your title')
    text = blocks.TextBlock(required=True, help_text="add additional text")

    class Meta:
        template = 'inc/post_block.html'
        icon = 'edit'
        label = 'Title & Text'


class RichtextBlock(blocks.RichTextBlock):

    class Meta:
        template = 'inc/richtext_block.html'
        icon = 'edit'
        label = 'Full RichText'


class SimpleRichtextBlock(blocks.RichTextBlock):

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = [
            'bold',
            'italic',
            'link',
        ]

    class Meta:
        template = 'inc/richtext_block.html'
        icon = 'edit'
        label = 'Simple RichText'


class CarouselBlock(blocks.StructBlock):
    items = blocks.ListBlock(
        blocks.StructBlock([
            ('image', ImageChooserBlock(required=True)),
            ('text', blocks.TextBlock(required=False, max_length=300)),
            ('button_url', blocks.URLBlock(required=False, help_text='Custom Url')),
        ])
    )

    class Meta:
        template = 'inc/carousel_block.html'
        icon = 'edit'
        label = 'Carousel'


class ButtonBlock(BlockSettings):
    url = blocks.CharBlock( max_length=500, blank=True, )
    label = blocks.CharBlock(required=False, help_text='Label')

    class Meta:
        template = 'inc/button_block.html'
        icon = 'edit'
        label = 'Button'