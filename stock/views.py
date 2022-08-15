
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.contrib import messages

from django.db.models import Q
from stock.models import Vehicle

# from stock.models import Vehicle


class StockView(ListView):
    """
    Generic class used to display vehicle display page

    """

    def get_queryset(self):
        queryset = Vehicle.objects.filter(available_sale=True)
        super().get_queryset()

        if 'q' in self.request.GET:
            query = self.request.GET['q']
            if not query:
                messages.error(self.request,
                               ("You didn't enter any search criteria!"))
                return queryset
            # attempt to implement muli-term search
            terms = self.request.GET['q'].split(' ')

            field_names = ["maker__maker", "model", "fuel__fuel", "year"]
            or_query = None
            query = None
            for term in terms:
                for field in field_names:
                    q = Q(**({"%s__icontains" % field: term}))
                    if or_query is None:
                        or_query = q
                    else:
                        or_query = or_query | q
                if query is None:
                    query = or_query
                else:
                    query = query and or_query
            queries = query
            vehicles = Vehicle.objects.filter(available_sale=True)
            queryset = vehicles.filter(queries)

        return queryset

    model = Vehicle
    template_name = "stock/stock.html"


class StockDetailView(DetailView):
    """
    Generic class used to display vehicle detail page

    """
    model = Vehicle
    template_name = "stock/stock_detail.html"
