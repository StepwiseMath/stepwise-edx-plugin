"""
Written by: Lawrence McDaniel
            https://lawrencemcdaniel.com

Date:   Jan-2022

Usage:  To enhance the behavior of the life cycle of the user session
"""
import logging

from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

log = logging.getLogger(__name__)

# coming in Maple
# from openedx_events.learning.signals import SESSION_LOGIN_COMPLETED


@receiver(user_logged_in)
def post_login(sender, user, request, **kwargs):
    log.info("stepwise_plugin received user_logged_in signal for {username}".format(username=user.username))


@receiver(user_logged_out)
def post_logout(sender, user, request, **kwargs):
    log.info("stepwise_plugin received user_logged_out signal for {username}".format(username=user.username))
