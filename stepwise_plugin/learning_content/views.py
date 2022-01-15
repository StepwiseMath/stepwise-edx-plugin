"""
the edx-platform parameter ENABLE_MKTG_SITE causes several site links
to use a custom setting stored in MKTG_URL_OVERRIDES

MKTG_URL_OVERRIDES["COURSES"] points here.

We need to determine which Wordpress site to redirect the user
based on their language preference.

"""
from django.shortcuts import redirect

from openedx.core.djangoapps.lang_pref import LANGUAGE_KEY
from openedx.core.djangoapps.user_api.preferences.api import get_user_preference


def list_by_locale(request):

    if request.user and request.user.is_authenticated:
        preferred_language = get_user_preference(request.user, LANGUAGE_KEY)

    if preferred_language == "es-419":
        return redirect("https://mx.stepwisemath.ai/learning-content/")

    return redirect("https://stepwisemath.ai/learning-content/")
