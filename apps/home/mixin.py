# *-* coding: utf-8 *-*
from django.core.exceptions import ImproperlyConfigured
from django.views.generic.base import ContextMixin
from django.http import HttpResponseRedirect


class UpdateMixin:
    """Provide the ability to delete objects."""
    success_url = None
    object = None
    queryset = None
    model = None
    pk_url_kwarg = 'pk'

    def update(self, request, *args, **kwargs):
        """
        Call the update() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.queryset
        if self.queryset is None:
            pk = kwargs.get(self.pk_url_kwarg)
            self.object = self.model.objects.get(pk=pk)
        success_url = self.get_success_url()
        self.object.save()
        return HttpResponseRedirect(success_url)

    # Add support for browsers which only accept GET and POST for now.
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # Add support for browsers which only accept GET and POST for now.
    def path(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get_success_url(self):
        if self.success_url:
            return self.success_url.format(**self.object.__dict__)
        else:
            raise ImproperlyConfigured(
                "No URL to redirect to. Provide a success_url.")
