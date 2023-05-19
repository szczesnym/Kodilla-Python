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

print('******************\033[92m Prin all series from library\033[0m*********************')
for serie in video_library.get_series():
    print(serie)
print('******************\033[92m Prin all movies from library\033[0m*********************')
for movie in video_library.get_movies():
    print(movie)

print('****************** Search of \033[92m yt \033[0m in library *********************')
for movie in video_library.search('yt'):
    print(movie)
print('****************** generate\033[92m single view \033[0m in library *********************')
video_library.generate_views()

print('****************** Generate\033[92m 10 views \033[0m in library *********************')
repeat(10, video_library.generate_views)

print('******************\033[92m Top 5 titles \033[0m in library *********************')
print('Top titles')
for movie in video_library.top_titles(5):
    print(movie)

video_library.generate_serie_season(title='Clone War: rebels', year=2004, genre='Sci-Fi', season_number=1,
                                    no_of_episodes=22)
print('******************Library after \033[92m Add Season \033[0m *********************')
for serie in video_library.get_series():
    print(serie)

print('Number of episodes of \033[92mClone War: rebels\033[0m -> ' +
      str(video_library.get_number_of_episodes('Clone War: rebels')))


