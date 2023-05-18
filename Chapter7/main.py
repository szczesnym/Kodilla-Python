from library import Library
#from series import Series
#from movie import Movie
from random import randrange


def repeat(count, func, *args):
    for i in range(count):
        func(*args)


video_library = Library()
video_library.load_data(file_name='movies.csv', typ='movies')
video_library.load_data(file_name='series.csv', typ='series')

for serie in video_library.get_series():
    print(serie)

for movie in video_library.get_movies():
    print(movie)

print('***************************************')
for movie in video_library.search('yt'):
    print(movie)
print('***************************************')
video_library.generate_views()

repeat(10, video_library.generate_views)

print('***************************************')
print('Top titles')
for movie in video_library.top_titles(5):
    print(movie)

print('***************************************')
print('Add seasons')
video_library.generate_serie_season(title='Clone War: rebels', year=2004, genre='Sci-Fi', season_number=1,
                                    no_of_episodes=22)

for serie in video_library.get_series():
    print(serie)