"""
Lawrence McDaniel - https://lawrencemcdaniel.com
Jan-2022

StepWise theming utility functions
"""

from ast import Str
from stepwise_plugin.models import Locale

def anchor(element_id: Str, prefered_language="en"):
    """
    id: an html anchor tag id value
    example: stepwise-about

    returns the URL and anchor element value based on the user's
    example
    """

    locale = Locale.objects.filter(element_id=element_id, lang=prefered_language).first()
    if not locale:
        # try a simpler variation of the language code.
        prefered_language = prefered_language[:2]
        locale = Locale.objects.filter(element_id=element_id, lang=prefered_language).first()

    if not locale:
        # try to grab the element in English.
        locale = Locale.objects.filter(element_id=element_id, lang="en").first()

    if not locale:
        return {}
    
    return {
        "url": locale.url,
        "value": locale.value
    }