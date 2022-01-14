"""
Lawrence McDaniel - https://lawrencemcdaniel.com
Jan-2022

StepWise theming utility functions
"""

from ast import Str
from openedx.core.djangoapps.lang_pref import LANGUAGE_KEY
from openedx.core.djangoapps.user_api.preferences.api import get_user_preference

# this repo
from stepwise_plugin.models import Locale

def anchor(user, element_id: Str):
    """
    id: an html anchor tag id value
    example: stepwise-about

    returns the URL and anchor element value based on the user's
    example
    """
    prefered_language = "en"
    if user.is_authenticated:
        prefered_language = get_user_preference(user, LANGUAGE_KEY)

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