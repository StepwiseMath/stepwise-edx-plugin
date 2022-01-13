"""
Lawrence McDaniel - https://lawrencemcdaniel.com
Aug-2021

User module App Configuration
"""
import logging

from django.apps import AppConfig

from edx_django_utils.plugins import PluginSettings, PluginURLs
from openedx.core.djangoapps.plugins.constants import ProjectType, SettingsType

log = logging.getLogger(__name__)


class UserConfig(AppConfig):
    name = "stepwise_user"
    label = "stepwise_user"
    verbose_name = "StepWise edx-platform user app modifications and enhancements"

    # See: https://edx.readthedocs.io/projects/edx-django-utils/en/latest/edx_django_utils.plugins.html
    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: name,
                PluginURLs.REGEX: "^stepwise/user/api/",
                PluginURLs.RELATIVE_PATH: "urls",
            }
        },
        PluginSettings.CONFIG: {
            ProjectType.LMS: {
                # uncomment these to activate
                # SettingsType.PRODUCTION: {PluginSettings.RELATIVE_PATH: "settings.production"},
                # SettingsType.COMMON: {PluginSettings.RELATIVE_PATH: "settings.common"},
            }
        },
    }

    def ready(self):
        log.debug("{label} is ready.".format(label=self.label))
