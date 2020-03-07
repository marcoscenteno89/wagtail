from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, PageChooserPanel, InlinePanel
from wagtail.core.fields import StreamField, RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core import blocks
from wagtail.contrib.settings.models import BaseSetting, register_setting
from . import blocks
    

class FlexPage(Page):
    template = "pages/flex_page.html"

    banner_title = models.CharField(max_length=100, blank=True, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"], default="Demo Test")
    banner_image = models.ForeignKey( 
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete = models.SET_NULL,
        related_name = "+"
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null = True,
        blank = True,
        on_delete = models.SET_NULL,
        related_name = "+"
    )
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("banner_title"),
            FieldPanel("banner_subtitle"),
            ImageChooserPanel("banner_image"),
            PageChooserPanel("banner_cta"),
        ], heading='Banner Options'),
    ]
    body = StreamField(
        [
            ('title_and_text', blocks.TitleAndTextBlock()),
            ('full_richtext', blocks.RichtextBlock()),
            ('simple_richtext', blocks.SimpleRichtextBlock()),
            ('cards', blocks.CardBlock()),
            ('carousel', blocks.CarouselBlock()),
            ('button', blocks.ButtonBlock()),
        ],
        null=True,
        blank=True,
    )
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            InlinePanel('carousel_images', label='Image'),
        ], heading="Carousel Images"),
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = 'Flex Page'
        verbose_name_plural = 'Flex Pages'
 
@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(blank=True, null=True, help_text='Facebook')
    twitter = models.URLField(blank=True, null=True, help_text='Twitter')
    youtube = models.URLField(blank=True, null=True, help_text='Youtube')
    google = models.URLField(blank=True, null=True, help_text='google')
    pinterest = models.URLField(blank=True, null=True, help_text='pinterest')
    linkedin = models.URLField(blank=True, null=True, help_text='linkedin')

    panels = [
        MultiFieldPanel([
            FieldPanel('facebook'),
            FieldPanel('twitter'),
            FieldPanel('youtube'),
            FieldPanel('google'),
            FieldPanel('pinterest'),
            FieldPanel('linkedin'),
        ], heading='Social Media Settings'),
    ]