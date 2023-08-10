from lib.artist_repository import ArtistRepository
from lib.database_connection import DatabaseConnection
from lib.album_repository import AlbumRepository

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        # "Runs" the terminal application.
        # It might:
        #   * Ask the user to enter some input
        #   * Make some decisions based on that input
        #   * Query the database
        #   * Display some output
        # We're going to print out the artists!
        print("Welcome to the music library manager!\n")

        print("What would you like to do?\n1 - List all albums\n2 - List all artists\n")

        counter = 0

        while counter == 0:
            selection = int(input("Enter your choice: "))
            if selection == 1:
                album_repository = AlbumRepository(self._connection)
                albums = album_repository.all()
                print("\nHere's the list of albums:")
                for album in albums:
                    print(f"{album.id} - {album.title}")
                counter += 1
            elif selection == 2:
                artist_repository = ArtistRepository(self._connection)
                artists = artist_repository.all()
                for artist in artists:
                    print(f"{artist.id} - {artist.name}")
                counter += 1
            else:
                selection = print("\nInvalid selection, please enter either 1 or 2\n")

if __name__ == '__main__':
    app = Application()
    app.run()
