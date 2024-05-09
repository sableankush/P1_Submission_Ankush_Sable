
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from facility_app.models import Facility

from django.contrib.gis.measure import D
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance
from facility_app.error_check import check_nearbyfacility_body, check_page_parameters
from facility_app.serializers import AllFacilitySerializer, NearByFacilitySerializer

class AllFacility(APIView):

    def get(self, request):
        try:
            err = check_page_parameters(self)
            if not err:
                page_number = abs(int(self.request.query_params.get('page', 1)))
                page_size = abs(int(self.request.query_params.get('size', 20)))
                last_record = page_number * page_size
                initial_record = last_record-page_size
                
                facility_available = Facility.objects.all().count()
                facilities = Facility.objects.all()[initial_record:last_record]
                serializer = AllFacilitySerializer(facilities, many=True)

                url = request.build_absolute_uri().split('?')[0]
                res = {
                    "previous": f'{url}?page={page_number-1}&size={page_size}' if page_number > 1 else None,
                    "next": f'{url}?page={page_number+1}&size={page_size}' if last_record < facility_available else None,
                    "facility_available": facility_available,
                    "facilities": serializer.data
                }
                return Response(res, status.HTTP_200_OK)
            else:
                return Response({"error": err}, status.HTTP_400_BAD_REQUEST)
        except:
            return Response(
                {"error": "failed to load data"},
                status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class NearByFacility(APIView):
     
    def get(self, request):
        try:
            err = check_page_parameters(self)
            if not err:
                body = request.data
                page_number = abs(int(self.request.query_params.get('page', 1)))
                page_size = abs(int(self.request.query_params.get('size', 20)))
                last_record = page_number * page_size
                initial_record = last_record-page_size

                err = check_nearbyfacility_body(body)
                if not err:
                    facility_type = body.get("facility_type").strip()
                    longitude = float(body.get("longitude").strip())
                    latitude = float(body.get("latitude").strip())
                    facility_count = int(body.get("facility_count").strip())
                    user_location = Point(longitude, latitude, srid=4326)
                    facility_available = Facility.objects.filter(facility_type=facility_type).annotate(distance=Distance('point', user_location)).order_by('distance')[0:facility_count].count()
                    facilities = Facility.objects.filter(facility_type=facility_type).annotate(distance=Distance('point', user_location)).order_by('distance')[initial_record:last_record if last_record <= facility_count else facility_count]
                    serializer = NearByFacilitySerializer(facilities, many=True)

                    url = request.build_absolute_uri().split('?')[0]
                    res = {
                        "previous": f'{url}?page={page_number-1}&size={page_size}' if page_number > 1 else None,
                        "next": f'{url}?page={page_number+1}&size={page_size}' if last_record < facility_available else None,
                        "facility_available": facility_available,
                        "facilities": serializer.data
                    }
                    return Response(res, status.HTTP_200_OK)
                else:
                    return Response({"error": err}, status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": err}, status.HTTP_400_BAD_REQUEST)
        except:
            return Response(
                {"error": "Failed to load data..."},
                status.HTTP_500_INTERNAL_SERVER_ERROR
            )
