from django.urls import include, path

urlpatterns = [
    path(
        'crudlfap',
        include(
            'mycrudlfap.urls',
            namespace='crudlfap',
        ),
    ),
]
