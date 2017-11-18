"""
Generic View Imports
"""
from __future__ import unicode_literals

from django.views.generic import TemplateView

# Create your views here.

class Home(TemplateView):
    """
    View pointing to User Dashboard
    """
    template_name = "dashboard.html"
