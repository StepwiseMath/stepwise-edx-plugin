Querium StepWise Plugin for Open edX
============================
[![hack.d Lawrence McDaniel](https://img.shields.io/badge/hack.d-Lawrence%20McDaniel-orange.svg)](https://lawrencemcdaniel.com)

Enhancements to the Open edX User model.

## Language Notes

### UserProfile.language

Language is deprecated and no longer used. Old rows exist that have
user-entered free form text values (ex. "English"), some of which have
non-ASCII values. You probably want UserPreference version of this, which
stores the user's preferred language code.


### openedx/core/djangoapps/lang_pref

Implements an app api to poll information about which languages are released
on this platform. Of particular interest: get_closest_released_language(target_language_code)

## StepWise API - Rover legacy app
Scaffolded with Django REST Framework Cookie Cutter.

## Stepwise Math Ecommerce Additional Configuration

This module provides course-level configuration for course payment deadline dates and
for maintaining course/section level lists of EOP students who are exempt from payments.

Data in these tables in referenced by templates in Rover edx-theme repo for decisioning
on whether to raise the Rover paywall.

admin.py
--------
To register models with [Django Admin Console app](https://docs.djangoproject.com/en/2.1/ref/contrib/admin/).


models.py
--------
All are Generic [Django Models](https://docs.djangoproject.com/en/2.1/topics/db/models/). Nothing noteworthy about any of these.
- Configuration

serializers.py
--------
Subclasses from [Django REST Framework Serializers](https://www.django-rest-framework.org/api-guide/serializers/) to serialize Django ORM model data into JSON representations.

urls.py
--------
[rest_framework router](https://www.django-rest-framework.org/api-guide/routers/) configuration for the REST api end points as well as introspection-based documentation

views.py
--------
implemented using [rest_framework ViewSets](https://www.django-rest-framework.org/api-guide/viewsets/). This is the simplest possible implementation, offering fully-functional list and detail views with default behavior.
