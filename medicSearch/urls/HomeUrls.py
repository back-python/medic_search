from django.urls import URLPattern, path
from medicSearch.views.HomeView import home_view

urlpatterns = [
    path('', home_view)
]