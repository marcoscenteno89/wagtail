from wagtail.core import blocks
from django.db import models
from wagtail.core.models import Orderable
from wagtail.images.blocks import ImageChooserBlock
from modelcluster.fields import ParentalKey
from wagtail.images.edit_handlers import ImageChooserPanel

class TitleAndTextBlock(blocks.StructBlock):
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


class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Add your title')
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('image', ImageChooserBlock(required=True)),
                ('title', blocks.CharBlock(required=True, max_length=40)),
                ('text', blocks.TextBlock(required=True, max_length=200)),
                ('button_page', blocks.PageChooserBlock(required=False)),
                ('button_url', blocks.URLBlock(required=False, help_text='this is a test')),
            ]
        )
    )

    class Meta:
        template = 'inc/card_block.html'
        icon = 'edit'
        label = 'Cards'


class CarouselBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Add your title')
    items = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('image', ImageChooserBlock(required=True)),
                ('title', blocks.CharBlock(required=True, max_length=40)),
                ('text', blocks.TextBlock(required=True, max_length=200)),
                ('button_page', blocks.PageChooserBlock(required=False)),
                ('button_url', blocks.URLBlock(required=False, help_text='this is a test')),
            ]
        )
    )

    class Meta:
        template = 'inc/carousel_block.html'
        icon = 'edit'
        label = 'Carousel'


class CarouselImages(Orderable):
    page = ParentalKey('flex.FlexPage', related_name='carousel_images')
    carousel_image = models.ForeignKey( 
        "wagtailimages.Image",
        null = True,
        blank = False,
        on_delete = models.SET_NULL,
        related_name = "+"
    )

    panels = [
        ImageChooserPanel('carousel_image')
    ]


class ButtonBlock(blocks.StructBlock):
    button_page = blocks.PageChooserBlock(required=False, help_text="If selected, this url will be used")
    button_url = blocks.URLBlock(required=False, help_text="If selected, this page will be used")
