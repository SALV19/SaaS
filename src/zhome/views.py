from django.shortcuts import render
import pathlib

from visits.models import PageVisits

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
  queryset = PageVisits.objects.filter(path=request.path)
  all_visits = PageVisits.objects.all()
  try:
    percent = queryset.count() * 100 / all_visits
  except:
    percent = 0
  my_title="Indiana Jones"
  my_context= {
    "page_title": my_title,
    "page_visits_count": queryset.count(),
    "percentage-visits": percent
  }
  path = request.path
  html_template ="home.html"
  PageVisits.objects.create(path=path)
  return render(request, html_template, my_context)