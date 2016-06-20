{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# -*- coding: utf-8 -*-
"""
{{ cookiecutter.project_slug }}
~~~~~~~~~~~~~~~~~~~
{{ cookiecutter.project_short_description }}
{% if is_open_source %}
:copyright: (c) {% now 'local', '%Y' %} by {{ cookiecutter.full_name }}
:licence: {{ cookiecutter.open_source_license }}, see LICENCE for more details
{%- endif %}
"""
from __future__ import absolute_import, unicode_literals
import logging

__version__ = '{{ cookiecutter.version }}'

__title__ = '{{ cookiecutter.project_name }}'
__summary__ = '{{ cookiecutter.project_short_description }}'
__uri__ = 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}'
__author__ = '{{ cookiecutter.full_name }}'
__email__ = '{{ cookiecutter.email }}'
{%- if is_open_source %}
__license__ == 'Copyright {% now 'local', '%Y' %} {{ cookiecutter.full_name }}'
{%- endif %}

logging.getLogger(__name__).addHandler(logging.NullHandler())
