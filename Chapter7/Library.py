from movie import Movie
from series import Series
import csv


def load_data(file_name, typ):
    return_list =[]
    csv.register_dialect('excel_file', delimiter=';', quoting=csv.QUOTE_NONE)
    if typ == 'series':
        fieldnames = ['episode_no', 'series', 'title', 'year', 'season', 'genre']
        with open(file_name, newline='') as csv_file:
            reader = csv.DictReader(csv_file, dialect='excel_file', fieldnames=fieldnames)
            for row in reader:
                temp_series = Series(title=row['title'], release_year=row['year'], genre=row['genre'],
                                     season=row['season'], episode_no=row['episode_no'])
                return_list.append(temp_series)
                print(row)
    elif typ == 'movies':
        fieldnames = ['title', 'year', 'genre']
        with open(file_name, newline='') as csv_file:
            reader = csv.DictReader(csv_file, dialect='excel_file', fieldnames=fieldnames)
            for row in reader:
                print(row)
                temp_movie = Movie(title=row['title'], release_year=row['year'], genre=row['genre'])
                return_list.append(temp_movie)
    else:
        pass
    return return_list


print(load_data('movies.csv', typ='movies', *library))
