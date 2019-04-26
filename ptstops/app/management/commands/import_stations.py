from django.core.management.base import BaseCommand, CommandError
from app.models import Route, Station
import csv

IMPORT_FILE = 'moscow_bus_stations.csv'


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(IMPORT_FILE, encoding='cp1251') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                station = Station.objects.create(latitude=row['Latitude_WGS84'],
                                                 longitude=row['Longitude_WGS84'],
                                                 name=row['Name'])
                csv_routes = row['RouteNumbers'].split(';')
                for item in csv_routes:
                    route, created = Route.objects.get_or_create(name=item)
                    station.routes.add(route)
