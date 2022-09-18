
"""
home app views
"""


from django.views.generic import TemplateView
from stock.models import Vehicle


# Create your views here.


class HomeView(TemplateView):
    """
    Generic class used to display home page

    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehicles'] = Vehicle.objects.filter(
                                            featured=True, available_sale=True)
        return context
    template_name = "home/home.html"


class LocationView(TemplateView):
    template_name = "home/location.html"
