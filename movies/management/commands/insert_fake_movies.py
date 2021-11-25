from django.core.management.base import BaseCommand
from faker import Faker

from movies.models import Movie, Actor


class Command(BaseCommand):

    def add_arguments(self, parser):

        self.stdout.write('You can choose quantity of created films with a help of --len="YOUR VALUE".Default value is 10.')
        parser.add_argument('--len', type=int, default=10)
        parser.add_argument('--year', type=int, default=2008)
        parser.add_argument('--runtime,', type=int, default=1)
        parser.add_argument('--rating', type=float, default=7.5)

    def handle(self, *args, **options):
        # Инициализация Faker
        faker = Faker()

        self.stdout.write('Creating new movies')
        for _ in range(options['len']):
            movie = Movie()
            actor = Actor()
            # fake имя для названия фильма при помощи faker
            new_title = ' '.join(faker.text().split()[:2])
            new_actor = ' '.join(faker.name())

            movie.name = new_title
            movie.year = options['year']
            # actor.name = new_actor

            for i in range(5):
                new_actor = faker.name()
                actor.name = new_actor
                # movie.actors += ''.join(actor.name)
                movie.actors += f"{''.join(actor.name)},"
            movie.save()
            actor.save()
            self.stdout.write(f'New movie was created: {movie}')


        self.stdout.write('Movies were created and added')

