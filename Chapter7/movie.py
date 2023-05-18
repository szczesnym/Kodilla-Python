class Movie:
    def __init__(self, title, release_year, genre):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self._display_count = 0

    @property
    def display_count(self):
        return self._display_count

    @display_count.setter
    def display_count(self, count):
        self._display_count = count

    def __str__(self):
        return f'{self.title} ({self.release_year})'

    def play(self):
        self._display_count += 1


