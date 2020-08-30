from django.core.management.base import BaseCommand, CommandError
from clients.models import Profile
from django.conf import settings
import environ
import googlemaps
import csv


env = environ.Env()
environ.Env.read_env()


class Command(BaseCommand):
    help = 'Populanting database with customers from a file.'

    def handle(self, *args, **kwargs):
        filename = settings.BASE_DIR / 'customers.csv'
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=",")
            next(reader, None)
            gmaps = googlemaps.Client(key=env.str("KEY_GOOGLE_MAPS"))
            for row in reader:
                print('Creating Profile id: {} name: {}'.format(row[0], row[1]))
                geocode_result = gmaps.geocode(row[6])
                location = geocode_result[0].get('geometry').get('location')
                lat = location.get('lat')
                lng = location.get('lng')
                obj = Profile(id=row[0], first_name=row[1], last_name=row[2], email=row[3], gender=row[4],
                              company=row[5], city=row[6], title=row[7], latitude=lat, longitude=lng)
                obj.save()

        print('Successfully imported customers.')
