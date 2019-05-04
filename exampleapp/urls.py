from django.urls import include, path

from . import views


app_name = 'exampleapp'


urlpatterns = [
    path(
        'examplemodel/',
        include(
            'exampleapp.examplemodel_urls',
            namespace='examplemodel',
        ),
    ),
]
