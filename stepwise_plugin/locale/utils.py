"""
Lawrence McDaniel - https://lawrencemcdaniel.com
Jan-2022

StepWise theming utility functions
"""

from ast import Str


def anchor(user,  id: Str):
    """
    id: an html anchor tag id value
    example: stepwise-about

    returns the URL and anchor element value based on the user's 
    example 
    """
    if not user.is_authenticated:
        prefered_language = 'en'


