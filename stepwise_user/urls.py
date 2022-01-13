"""
Lawrence McDaniel - https://lawrencemcdaniel.com
Aug-2021

Cabinet Office User Module URLs.
"""
# Django
from django.conf.urls import url
from django.conf import settings

# this repo
from .views import dashboard

app_name = "stepwise_user"

urlpatterns = [
    url(fr"^{settings.USERNAME_PATTERN}$/dashboard", dashboard, name="stepwise_dashboard"),
]
