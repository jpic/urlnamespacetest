import os
import pytest

from django.conf import settings
from django.urls import path, reverse, URLPattern, URLResolver
from django.urls.resolvers import RoutePattern


os.environ['DJANGO_SETTINGS_MODULE'] = 'urlnamespacetest.settings'


def test_natural():
    expected = '/crudlfapexampleappexamplemodel/list'
    res = reverse('crudlfap:exampleapp:examplemodel:list')
    assert res == expected


crudlfap = URLResolver(
    pattern=RoutePattern('crudlfap/'),
    urlconf_name=[],
    namespace='crudlfap',
    app_name='crudlfap',
)
exampleapp = URLResolver(
    pattern=RoutePattern('exampleapp/'),
    urlconf_name=[],
    namespace='exampleapp',
    app_name='exampleapp',
)
examplemodel = URLResolver(
    pattern=RoutePattern('examplemodel/'),
    urlconf_name=[],
    namespace='examplemodel',
    app_name='examplemodel',
)
examplemodel.url_patterns = [
    path(
        'list',
        lambda request: None,
        name='list',
    ),
]
exampleapp.url_patterns = [examplemodel]
crudlfap.url_patterns = [exampleapp]
urlpatterns = [crudlfap]


@pytest.mark.urls('test_reverse')
def test_other():
    res = reverse('crudlfap:exampleapp:examplemodel:list')
    expected = '/crudlfap/exampleapp/examplemodel/list'
    assert expected == res
