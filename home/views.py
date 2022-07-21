
"""
home app views
"""


from django.views.generic import TemplateView

# Create your views here.


class HomeView(TemplateView):
    """
    Generic class used to display home page

    """
    template_name = "home/home.html"
