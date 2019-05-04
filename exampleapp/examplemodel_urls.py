from django.urls import path

from . import views


app_name = 'exampleapp'


urlpatterns = [
    path(
        'create',
        views.ExampleModelCreate.as_view(),
        name='create',
    ),
    path(
        'list',
        views.ExampleModelList.as_view(),
        name='list',
    ),
]
