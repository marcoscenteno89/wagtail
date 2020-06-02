from django.db import models
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import ObjectList, TabbedInterface, MultiFieldPanel, FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from modelcluster.fields import ParentalKey
from flex import blocks


class Product(models.Model):

    template = 'services/product_block.html'
    title = models.CharField(max_length=100, blank=False, null=False, default='Title')
    price = models.CharField(max_length=100, blank=False, null=False)
    duration = models.CharField(max_length=100, blank=False, null=False)
    cta_label = models.CharField(max_length=100, blank=False, null=False)
    cta_link = models.CharField(max_length=100, blank=False, null=False)
    service_type = models.CharField(max_length=100, blank=False, null=False)
    company = models.CharField(max_length=100, blank=False, null=False)
    description =models.CharField(max_length=100, blank=False, null=False)
    panels = MultiFieldPanel([
        FieldPanel('title'),
        FieldPanel('price'),
        FieldPanel('duration'),
        FieldPanel('cta_label'),
        FieldPanel('cta_link'),
        FieldPanel('service_type'),
        FieldPanel('description'),
    ], heading='Body', classname='collapsible'),

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Promotion(models.Model):
    template = 'services/promotion_block.html'
    title = models.CharField(max_length=100, blank=False, null=False, default='Title')
    promo = models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete = models.SET_NULL,
        related_name = "+",
    )
    cta_label = models.CharField(max_length=100, blank=False, null=False)
    cta_link = models.CharField(max_length=100, blank=False, null=False)
    company = models.CharField(max_length=100, blank=False, null=False)
    promo_type = models.CharField(max_length=100, blank=False, null=False)    
    expiration_date = models.DateField()
    panels = MultiFieldPanel([
        FieldPanel('title'),
        ImageChooserPanel('promo'),
        FieldPanel('cta_label'),
        FieldPanel('cta_link'),
        FieldPanel('company'),
        FieldPanel('promo_type'),
        FieldPanel('expiration_date'),
    ], heading='body', classname='collapsible'),

    class Meta:
        verbose_name = 'Promotion'
        verbose_name_plural = 'Promotions'


class CompanyPage(Page):
    template = 'services/company_page.html'
    logo = models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete = models.SET_NULL,
        related_name = "+",
    )
    intro = models.CharField(max_length=1000, blank=False, null=False)
    package_category = models.CharField(max_length=1000, blank=False, null=False)
    smallprint = models.CharField(max_length=1000, blank=False, null=False)

    editor = StreamField([
            ('title_and_text', blocks.TitleAndTextBlock()),
            ('full_richtext', blocks.RichtextBlock()),
            ('carousel', blocks.CarouselBlock()),
            ('button', blocks.ButtonBlock()),
        ], null=True, blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('logo'),
        FieldPanel('intro'),
        FieldPanel('package_category'),
        FieldPanel('smallprint'),
        StreamFieldPanel('editor'),
    ]

    panels = MultiFieldPanel([
        FieldPanel('title'),
        ImageChooserPanel('promo'),
        FieldPanel('cta_label'),
        FieldPanel('cta_link'),
        FieldPanel('company'),
        FieldPanel('promo_type'),
        FieldPanel('expiration_date'),
    ], heading='body', classname='collapsible'),

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'