class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(self)
        Song.add_to_artists(self)
        Song.add_to_genre_count(self)
        Song.add_to_artist_count(self)
        
    def add_song_to_count():
        Song.count += 1


    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)
        else:
            print("Genre already exists in library")

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)
        else:
            print("Artist already exists in library")

    def add_to_genre_count(self):
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artist_count(self):
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1