# To include this database in your Django app, you will need to modify your settings.py
# module.
#
# If you have no other databases, you could add:
#     from sqlazure_django import DATABASES
#
# Alternatively, you could use:
#     import sqlazure_django
#     DATABASES['sqlazure'] = sqlazure_django.CONFIG
#

{% if cookiecutter.password_in_environment == 'y' %}import os
{% endif %}
CONFIG = {
    'ENGINE': 'sql_server.pyodbc',
{% for kv in cookiecutter.connection_string.split(';') %}{% set k = kv.partition("=")[0].lower() %}{% set v = kv.partition("=")[2] %}{% if k == "server" %}    'HOST': '{{v}}',
{% elif k == "database" %}    'NAME': '{{v}}',
{% elif k == "uid" %}    'USER': '{{v}}',
{% elif k == "pwd" and cookiecutter.password_in_environment == 'n' %}    'PASSWORD': '{{v}}',
{% endif %}{% endfor %}{% if cookiecutter.password_in_environment == 'y' %}    'PASSWORD': os.getenv('DB_PASSWORD'),
{% endif %}    'OPTIONS': {
        'port': '',
        'timeout': 30,
    }
}

DATABASES = { 'default': CONFIG }
