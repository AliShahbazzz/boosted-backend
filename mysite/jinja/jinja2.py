from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from resume.templatetags.split import *


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    env.filters.update({
        'split': split,
        'get_range': get_range,
        'join_var': join_var,
        'get_project': get_project,
        'get_certificate': get_certificate,
        'get_experience': get_experience
    })
    return env
