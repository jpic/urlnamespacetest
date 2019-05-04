from django.urls import include, path


app_name = 'mycrudlfap'

urlpatterns = [
    path(
        'exampleapp',
        include(
            'exampleapp.urls',
            namespace='exampleapp',
        ),
    ),
]
