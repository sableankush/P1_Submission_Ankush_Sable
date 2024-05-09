import csv
import os, sys
import django

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
parent = parent.replace('/facility_app', '')
sys.path.append(parent)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "World_Needs_More_Food_Trucks.settings")
django.setup()

from facility_app.models import Facility
from django.contrib.gis.geos import fromstr

def import_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            lon = row['Longitude'] if row['Longitude'] != "" else 0.0
            lat = row['Latitude'] if row['Latitude'] != "" else 0.0

            Facility.objects.create(
                location_id = row['locationid'] if row['locationid'] != "" else None,
                applicant = row['Applicant'] if row['Applicant'] != "" else None,
                facility_type = row['FacilityType'] if row['FacilityType'] != "" else None,
                cnn = row['cnn'] if row['cnn'] != "" else None,
                location_description = row['LocationDescription'] if row['LocationDescription'] != "" else None,
                address = row['Address'] if row['Address'] != "" else None,
                blocklot = row['blocklot'] if row['blocklot'] != "" else None,
                block = row['block'] if row['block'] != "" else None,
                lot = row['lot'] if row['lot'] != "" else None,
                permit = row['permit'] if row['permit'] != "" else None,
                status = row['Status'] if row['Status'] != "" else None,
                foodItems = row['FoodItems'] if row['FoodItems'] != "" else None,
                x = row['X'] if row['X'] != "" else None,
                y = row['Y'] if row['Y'] != "" else None,
                latitude = lat,
                longitude = lon,
                point = fromstr(f'POINT({lon} {lat})', srid=4326),
                schedule = row['Schedule'] if row['Schedule'] != "" else None,
                dayshours = row['dayshours'] if row['dayshours'] != "" else None,
                noi_sent = row['NOISent'] if row['NOISent'] != "" else None,
                approved = row['Approved'] if row['Approved'] != "" else None,
                received = row['Received'] if row['Received'] != "" else None,
                prior_permit = row['PriorPermit'] if row['PriorPermit'] != "" else None,
                expiration_date = row['ExpirationDate'] if row['ExpirationDate'] != "" else None,
                location = row['Location'] if row['Location'] != "" else None,
                fire_prevention_districts = row['Fire Prevention Districts'] if row['Fire Prevention Districts'] != "" else None,
                police_districts = row['Police Districts'] if row['Police Districts'] != "" else None,
                supervisor_districts = row['Supervisor Districts'] if row['Supervisor Districts'] != "" else None,
                zip_codes = row['Zip Codes'] if row['Zip Codes'] != "" else None,
                neighborhoods_old = row['Neighborhoods (old)'] if row['Neighborhoods (old)'] != "" else None
            )

if __name__ == '__main__':
    my_path = os.path.abspath(os.path.dirname(__file__))
    csv_file_path = os.path.join(my_path, "food-truck-data.csv")
    import_data(csv_file_path)