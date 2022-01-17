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
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie

from opaque_keys.edx.keys import CourseKey
from common.djangoapps.student.models import CourseEnrollment
from xmodule.modulestore.django import modulestore


from .utils import set_language_preference

log = logging.getLogger(__name__)


@login_required
@ensure_csrf_cookie
def student_dashboard(request):
    """
    Called from Wordpress marketing sites. Facilitates some preprocessing
    prior to opening the Open edX dashboard view.

    Defined params:
    "language": the default language for this referrer. example: es-419
    "enroll": a CourseKey. we should attempt to enroll the user in this course

    example url:
    https://web.stepwisemath.ai/stepwise/dashboard?lang=ex-419,enroll=edX+DemoX+Demo_Course
    """

    # should always be true, but it'd potentially be a trainwreck if we called
    # set_language_preference() at scale on the Django anonymous user.
    # so, qualifying the authentication just in case :O
    if request.user and request.user.is_authenticated:
        set_language_preference(request)

    # if there's an ´enroll´ param then parse it and try to enroll the the user in the course
    enroll_in = request.GET.get("enroll")
    if enroll_in:
        log.info("student_dashboard() received enroll param of {enroll_in}".format(enroll_in=enroll_in))

        course_key = None
        course = None

        try:
            course_key = CourseKey.from_string(enroll_in)
        except:
            log.warning(
                "student_dashboard() received an invalid CourseKey string in the enroll url param. Ignoring. value was: {enroll_in}".format(
                    enroll_in=enroll_in
                )
            )

        if course_key:
            try:
                course = modulestore().get_course(course_key)
            except Exception as e:
                log.warning(
                    "student_dashboard() encountered a handled exception while attempting to initialize course object for course key {enroll_in}. Exception: {e}".format(
                        enroll_in=enroll_in, e=e
                    )
                )

            try:
                # attempt to pre-enroll the user using the default enrollment mode.
                # if the user is already enrolled then this will be a no-op
                #
                # Either way however, we want to redirect the user to the course summary page,
                # assuming that the course has already started.
                CourseEnrollment.enroll(request.user, course_key=course_key)
                if course.has_started():
                    return redirect(reverse("openedx.course_experience.course_home", kwargs={"course_id": course_key}))
            except Exception as e:
                log.warning(
                    "student_dashboard() encountered a handled exception while attempting to enroll user {username} in the course {enroll_in}. Exception: {e}".format(
                        username=request.user.username, enroll_in=enroll_in, e=e
                    )
                )

    return redirect(reverse("dashboard"))
