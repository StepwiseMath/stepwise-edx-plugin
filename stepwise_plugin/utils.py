import logging
from django.conf import settings
from urllib.parse import urlparse

from openedx.core.djangoapps.lang_pref.api import get_closest_released_language
from openedx.core.djangoapps.lang_pref import LANGUAGE_KEY
from openedx.core.djangoapps.user_api.preferences.api import get_user_preference, set_user_preference

log = logging.getLogger(__name__)


def set_language_preference(request):
    """
    Preemptively set a language code preference based on
    1.) a language param that might be passed in the http request
    2.) the 2-character subdomain of the referrer. example mx.stepwisemath.ai == 'mx'
    """
    if not request.user or not request.user.is_authenticated:
        return None

    preferred_language = get_user_preference(request.user, LANGUAGE_KEY)
    if preferred_language:
        log.info(
            "user {username} (1) prefers language {preferred_language}".format(
                username=request.user.username, preferred_language=preferred_language
            )
        )
        return None

    # 2.) language code might be passed in as a parameter
    language_param = request.GET.get("language")
    if language_param:
        closest_lang = get_closest_released_language(language_param)
        log.info(
            "stepwise_plugin.utils.set_language_preference() (2) detected language param={language_param}. closest installed={closest_lang}".format(
                language_param=language_param, closest_lang=closest_lang
            )
        )
        set_user_preference(request.user, LANGUAGE_KEY, closest_lang)
        return None

    # 3.) try infer a language preference from the referring host
    referrer = urlparse(request.META.get("HTTP_REFERER", "Direct"))
    referrer_domain = referrer.netloc
    if referrer_domain and referrer_domain[:2].lower() == "mx":
        closest_lang = get_closest_released_language("es_MX")
        log.info(
            "stepwise_plugin.utils.set_language_preference() (3) detected referrer_domain={referrer_domain}. closest installed={closest_lang}".format(
                referrer_domain=referrer_domain, closest_lang=closest_lang
            )
        )
        set_user_preference(request.user, LANGUAGE_KEY, closest_lang)
        return None

    # 4.) defer to the language preference from openedx cookie
    # this case is taken care of by openedx.core.djangoapps.lang_pref.middleware.LanguagePreferenceMiddleware
    # cookie_lang_pref = request.COOKIES.get(settings.LANGUAGE_COOKIE, None)
