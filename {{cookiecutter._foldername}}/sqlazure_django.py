{% if cookiecutter.password_in_environment == 'y' %}import os
{% endif %}
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
{% for kv in cookiecutter.connection_string.split(';') %}{% set k = kv.partition("=")[0].lower() %}{% set v = kv.partition("=")[2] %}{% if k == "server" %}        'HOST': '{{v}}',
{% elif k == "database" %}        'NAME': '{{v}}',
{% elif k == "uidX" %}        'USERX': '{{v}}',
{% elif k == "uid" %}        'USER': '{{v}}',
{% elif k == "pwd" and cookiecutter.password_in_environment == 'n' %}        'PASSWORD': '{{v}}',
{% endif %}{% endfor %}{% if cookiecutter.password_in_environment == 'y' %}        'PASSWORD': os.getenv('DB_PASSWORD'),
{% endif %}        'OPTIONS': {
            'port': '',
            'timeout': 30,
        }
    }
}
