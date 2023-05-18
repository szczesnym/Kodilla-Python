from movie import Movie


def format_number(item):
    if len(str(item)) > 1:
        return item
    else:
        return '0' + str(item)


class Series(Movie):
    def __init__(self, episode_no, season, serie_title,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_no = episode_no
        self.season = season
        self.serie_title = serie_title

    def __str__(self):
        return f'{self.title} S{str(format_number(self.season))}E{str(format_number(self.episode_no))}'

