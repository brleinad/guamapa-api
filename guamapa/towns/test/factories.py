import factory


class TownFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'towns.Town'
        django_get_or_create = ('name',)

    id = factory.Faker('uuid4')
    name = factory.Faker('name')
    # position = factory.Faker('position')
    # elevation = factory.Faker('elevation')
    # population = factory.Fake('population')
    # description = factory.Fake('description')