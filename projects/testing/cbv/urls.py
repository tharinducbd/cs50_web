from django.urls import path
from django.views.generic import TemplateView

from cbv.views import Ex2View


app_name = 'cbv'

urlpatterns = [
    # extra_context Attribute from ContextMixin - keyward argument for as_view()
    path('ex1/', TemplateView.as_view(template_name='cbv/ex1.html',
                                     extra_context={'title': 'Custom Title'})),
    path('ex2/', Ex2View.as_view(), name='ex2')
]
