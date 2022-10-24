
"""
home app views
"""


from django.views.generic import TemplateView
from stock.models import Vehicle



class HomeView(TemplateView):
    """
    Generic class used to display home page

    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # create trade_flag if soes not exist
        if 'trade_flag' in self.request.session:
            pass
        else:
            self.request.session['trade_flag'] = False
        # filter vehicles to add featured vehicles to carousel
        context['vehicles'] = Vehicle.objects.filter(
                                            featured=True, available_sale=True)
        return context
    template_name = "home/home.html"


class LocationView(TemplateView):
    """
    Displays map
    """
    template_name = "home/location.html"
