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

python -m pip install --upgrade build

sudo rm -r build
sudo rm -r dist
#sudo rm -r edx_oauth2_wordpress_backend.egg-info

python3 -m build --sdist ./
python3 -m build --wheel ./

python3 -m pip install --upgrade twine
twine check dist/*

# PyPi test
twine upload --skip-existing --repository testpypi dist/*

# PyPi
#twine upload --skip-existing dist/*
