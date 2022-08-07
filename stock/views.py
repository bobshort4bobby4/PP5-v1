from django.views.generic import ListView
from stock.models import Vehicle
# from stock.models import Vehicle


class StockView(ListView):
    """
    Generic class used to display vehicle display page

    """

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['vehicles'] = Vehicle.objects.filter(featured=True)
    #     return context
    model = Vehicle
    template_name = "stock/stock.html"
