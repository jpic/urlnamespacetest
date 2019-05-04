from django.views import generic

from .models import ExampleModel


class ExampleModelList(generic.ListView):
    model = ExampleModel


class ExampleModelCreate(generic.CreateView):
    model = ExampleModel
