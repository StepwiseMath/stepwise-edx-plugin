"""
Written by: Lawrence McDaniel
            https://lawrencemcdaniel.com

Date:   Jan-2022

Usage:  To intercept http requests so that can do things like:
            - set environment variables, like the language code
            - redirect the user elsewhere, like say, an onboarding page
            - update user profile data
"""
import logging
from django.shortcuts import redirect
from django.urls import reverse

from common.djangoapps.student.views import student_dashboard as lms_student_dashboard

from .utils import set_language_preference

log = logging.getLogger(__name__)


def student_dashboard(request):

    if request.user and request.user.is_authenticated:
        set_language_preference(request)

    return redirect(reverse('dashboard'))
    #return lms_student_dashboard(request)
