from rest_framework import serializers

from vehicles.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            'id',
            'name',
            'alias',
            'creation_date',
            'edit_date',
            'company',
            'vehicle_type',
            'gps_id'
        ]
