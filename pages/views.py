from django.views.generic import TemplateView
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from .models import Hospital
from geopy.distance import geodesic
import geopy.geocoders

class HomePageView(TemplateView):
    template_name = "pages/index.html"

def about(request):
    return render(request, 'pages/about.html')


def hospital_finder(request):
    hospitals = []
    search_query = request.GET.get("search", "")

    if search_query:
        hospitals = Hospital.objects.filter(pin_code=search_query)

    return render(request, "pages/index.html", {"hospitals": hospitals, "search_query": search_query})


