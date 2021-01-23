import factory
from faker.providers import BaseProvider
from django.contrib.gis.geos import Point

class GeoPointProvider(BaseProvider):

    # uses faker.providers.geo
    def geo_point(self, **kwargs):
        kwargs['coords_only'] = True
        kwargs['country_code'] = 'GT'
        faker = factory.faker.faker.Faker()
        coords = faker.local_latlng(**kwargs)
        return Point(x=float(coords[1]), y=float(coords[0]), srid=4326)

    def geojson_point(self, **kwargs):
        kwargs['coords_only'] = True
        kwargs['country_code'] = 'GT'
        faker = factory.faker.faker.Faker()
        coords = faker.local_latlng(**kwargs)
        return {"type": "Point", "coordinates": [ float(coords[1]), float(coords[0]) ]}

        
        
factory.Faker.add_provider(GeoPointProvider)


class TownModelFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'towns.Town'
        django_get_or_create = ('name',)

    id = factory.Faker('uuid4')
    name = factory.Faker('city')
    location = factory.Faker('geo_point')
    # elevation = factory.Faker('number')
    # population = factory.Fake('number')
    # description = factory.Fake('text')

class TownFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'towns.Town'
        django_get_or_create = ('name',)

    id = factory.Faker('uuid4')
    name = factory.Faker('city')
    location = factory.Faker('geojson_point')
    # elevation = factory.Faker('number')
    # population = factory.Fake('number')
    # description = factory.Fake('text')