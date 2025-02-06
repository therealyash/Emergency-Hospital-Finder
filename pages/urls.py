from django.urls import path
from .views import HomePageView, about, hospital_finder

app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
path("find-hospitals/", hospital_finder, name="hospital_finder"),
    path("about/", about, name="about"),
]
