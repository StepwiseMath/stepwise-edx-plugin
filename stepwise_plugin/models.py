from __future__ import absolute_import
from django.db import models
from django.utils.translation import ugettext as _

from model_utils.models import TimeStampedModel

class Locale(TimeStampedModel):
    """
    Stores localized urls and translated html tag element values by language code
    Used in conjunction with Mako templates to localize StepWise specific page content
    such as footer links.
    """
    languages = (
        ('en', 'English'),
        ('es-419', 'Español (Latinoamérica)'),  # Spanish (Latin America)
        ('pt-pt', 'Português (Portugal)'),  # Portuguese (Portugal)
    )
    class Meta:
        unique_together = ("element_id", "lang")

    element_id = models.CharField(
        blank=False,
        help_text=_(u"An html element id. Example: stepwise-locale-contact"),
    )
    lang = models.CharField(
        blank=False,
        choices=languages
        help_text=_(u"A language code. Examples: en, en-US, es, es-419, es-MX"),
    )
    url = models.URLField(
        blank=False,
        help_text=_(u"URL for for anchor tag for this language. Example: https://mx.stepwisemath.ai/contact/"),
    )
    value = models.CharField(
        blank=False,
        help_text=_(u"The text value of this html element. Example: Contacto"),
    )

    def __str__(self):
        return self.element_id + ' - ' + self.lang

class Configuration(models.Model):
    u"""
    Creates the Rover Stepwise configuration table for api settings.
    """
    DEVELOP = u"dev"
    TEST = u"test"
    PRODUCTION = u"prod"

    configuration_type = (
        (DEVELOP, _(u"Development")),
        (TEST, _(u"Testing / QA")),
        (PRODUCTION, _(u"Production")),
    )

    type = models.CharField(
        max_length=24,
        blank=False,
        primary_key=True,
        choices=configuration_type,
        default=DEVELOP,
        unique=True,
        help_text=_(u"Type of Open edX environment in which this configuration will be used."),
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    stepwise_host = models.URLField(
        max_length=255, blank=True, help_text=_(u"the URL pointing to the Querium Stepwise Server.")
    )

    def __str__(self):
        return self.type
