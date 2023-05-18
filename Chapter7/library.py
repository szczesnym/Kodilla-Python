from random import randrange
from faker import Faker
from faker.providers import company
from movie import Movie
from series import Series
import csv


class Library:
    library = []

    def load_data(self, file_name, typ):
        return_list =[]
        csv.register_dialect('excel_file', delimiter=';', quoting=csv.QUOTE_NONE)
        if typ == 'series':
            fieldnames = ['episode_no', 'series', 'title', 'year', 'season', 'genre']
            with open(file_name, newline='') as csv_file:
                reader = csv.DictReader(csv_file, dialect='excel_file', fieldnames=fieldnames)
                for row in reader:
                    temp_series = Series(title=row['title'], release_year=row['year'], genre=row['genre'],
                                         season=row['season'], episode_no=row['episode_no'], serie_title=row['series'])
                    self.library.append(temp_series)
                    print(row)
        elif typ == 'movies':
            fieldnames = ['title', 'year', 'genre']
            with open(file_name, newline='') as csv_file:
                reader = csv.DictReader(csv_file, dialect='excel_file', fieldnames=fieldnames)
                for row in reader:
                    #print(row)
                    temp_movie = Movie(title=row['title'], release_year=row['year'], genre=row['genre'])
                    #print(type(temp_movie))
                    self.library.append(temp_movie)

    def get_movies(self):
        return [movie for movie in sorted(self.library, key=lambda item: item.title) if not isinstance(movie, Series)]

    def get_series(self):
        return [serie for serie in sorted(self.library, key=lambda item: item.title) if isinstance(serie, Series)]

    def search(self, search_key):
        return [item for item in self.library if search_key in item.title]

    def generate_views(self):
        item_no = randrange(len(self.library))
        print(f'Item no:{item_no}')
        print(f'Random item:{self.library[item_no]}')
        print(f'Views before increase:{self.library[item_no].display_count}')
        self.library[item_no].display_count = randrange(100)
        print(f'Views AFTER increase:{self.library[item_no].display_count}')

    def top_titles(self, top_count):
        return [item for item in sorted(self.library, key=lambda item:item.display_count, reverse=True)][:top_count]

    def generate_serie_season(self, title, year, genre, season_number, no_of_episodes):
        fake = Faker()
        fake.add_provider(company)
        for i in range(no_of_episodes):
            self.library.append(Series(episode_no=i, season=season_number, title=fake.catch_phrase(), release_year=year,
                                       genre=genre, serie_title=title))

