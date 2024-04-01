from typing import Any
from django.views.generic.base import TemplateView

from cbv.models import Post


class Ex2View(TemplateView):

    """TemplateResponseMixin
    Provides a mechanism to construct a TemplateResponse, given suitable context.
    Attributes:
    """
    template_name = "cbv/ex2.html"
    # template_engine = The NAME of a template engine to use for loading the template. (Jinja2, Genshi)
    # response_class = Custom template loading or custom context object instantiation.
    # content_type = Default Django uses 'text/html'

    """ get_context_data(**kwargs) is a method inherited from ContentMixin. """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.get(id=1)
        context['data'] = "Context Data fro Ex2"
        return context
