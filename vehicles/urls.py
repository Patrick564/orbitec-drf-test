from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from vehicles.views import VehicleList, VehicleDetail


urlpatterns = [
    path('vehicles/', VehicleList.as_view()),  # type: ignore
    path('vehicles/<int:pk>', VehicleDetail.as_view())  # type: ignore
]

urlpatterns = format_suffix_patterns(urlpatterns)
