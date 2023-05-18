class Movie:
    def __init__(self, title, release_year, genre):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self._display_count = 0

    def __str__(self):
        return f'{self.title} ({self.release_year})'

    def play(self):
        self._display_count += 1


