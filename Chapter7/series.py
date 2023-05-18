from movie import Movie


class Series(Movie):
    def __init__(self, episode_no, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_no = episode_no
        self.season = season

    def __str__(self):
        return f'{self.title} S{str(self.season)}E{str(self.episode_no)}'
