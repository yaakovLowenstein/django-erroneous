import sys
import traceback

from django.core.signals import got_request_exception
from django.dispatch.dispatcher import receiver
from django.http import Http404
from django.views.debug import ExceptionReporter

from .models import Error


@receiver(got_request_exception)
def create_from_exception(sender, request=None, *args, **kwargs):
    """
    Handles the exception upon receiving the signal.
    """
    kind, info, data = sys.exc_info()
    if not issubclass(kind, Http404):

        error = Error.objects.create(
            kind=kind.__name__,
            html=ExceptionReporter(request, kind, info, data).get_traceback_html(),
            path=request.build_absolute_uri(),
            info=info,
            data="\n".join(traceback.format_exception(kind, info, data)),
        )
        error.save()
