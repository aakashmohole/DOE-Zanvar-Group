from django.urls import path
from .views import FilterDoeDataView

urlpatterns = [
    path('filter-doe/', FilterDoeDataView.as_view(), name='filter-doe'),
]
