"""
Lawrence McDaniel - https://lawrencemcdaniel.com
Aug-2021

Querium StepWise API App Configuration
"""
import logging

from django.apps import AppConfig

from edx_django_utils.plugins import PluginSettings, PluginURLs
from openedx.core.djangoapps.plugins.constants import ProjectType, SettingsType

log = logging.getLogger(__name__)


class StepwiseApiConfig(AppConfig):
    name = "stepwise_api"
    label = "stepwise_api"
    verbose_name = "Querium Stepwise Configuration for Open edX"

    # See: https://edx.readthedocs.io/projects/edx-django-utils/en/latest/edx_django_utils.plugins.html
    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: name,
                PluginURLs.REGEX: "^stepwise/",
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