from rest_framework import generics
from rest_framework import mixins

from vehicles.models import Vehicle
from vehicles.serializers import VehicleSerializer


class VehicleList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    """
    List all vehicles in the database and create news.
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request=request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class VehicleDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    """
    Details of all vehicles and edit or delete.
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
