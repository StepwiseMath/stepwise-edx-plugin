#!/bin/sh
#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com
#
# date:       oct-2022
#
# usage:      a work in progress. build package and upload to PyPi.
#             https://pypi.org/project/stepwise-edx-plugin/
#             https://pypi.org/project/stepwise-edx-plugin-lpm0073/
#
#------------------------------------------------------------------------------

./build.sh

# PyPi test
twine upload --skip-existing --repository testpypi dist/*

# PyPi
#twine upload --skip-existing dist/*
