from rest_framework import serializers
from facility_app.models import Facility

class AllFacilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Facility
        exclude = ('point', 'created', 'updated')

class NearByFacilitySerializer(serializers.ModelSerializer):
    closest_distance = serializers.SerializerMethodField()

    def get_closest_distance(self, obj):
        return f'{obj.distance.m} m'

    class Meta:
        model = Facility
        exclude = ('point', 'created', 'updated')
