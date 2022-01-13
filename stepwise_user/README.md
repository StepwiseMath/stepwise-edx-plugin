StepWise User Module
==========================
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
