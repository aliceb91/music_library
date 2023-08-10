from lib.album_repository import AlbumRepository
from lib.album import Album

def test_get_all_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    albums = repository.all()
    assert albums == [
        Album("Doolittle", 1989, 1, 1),
        Album("Surfer Rosa", 1988, 1, 2),
        Album("Waterloo", 1974, 2, 3),
        Album("Super Trouper", 1980, 2, 4),
        Album("Bossanova", 1990, 1, 5),
        Album("Lover", 2019, 3, 6),
        Album("Folklore", 2020, 3, 7),
        Album("I Put a Spell on You", 1965, 4, 8),
        Album("Baltimore", 1978, 4, 9),
        Album("Here Comes the Sun", 1971, 4, 10),
        Album("Fodder on My Wings", 1982, 4, 11),
        Album("Ring Ring", 1973, 2, 12)
    ]

def test_find_specific_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find(4)
    assert album == Album("Super Trouper", 1980, 2, 4)

def test_create_new_album(db_connection):
    # Given an Album object
    # It inserts that object into the albums table.
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    album = Album("Red", 2012, 3)
    repository.create(album)
    albums = repository.all()
    assert albums == [
        Album("Doolittle", 1989, 1, 1),
        Album("Surfer Rosa", 1988, 1, 2),
        Album("Waterloo", 1974, 2, 3),
        Album("Super Trouper", 1980, 2, 4),
        Album("Bossanova", 1990, 1, 5),
        Album("Lover", 2019, 3, 6),
        Album("Folklore", 2020, 3, 7),
        Album("I Put a Spell on You", 1965, 4, 8),
        Album("Baltimore", 1978, 4, 9),
        Album("Here Comes the Sun", 1971, 4, 10),
        Album("Fodder on My Wings", 1982, 4, 11),
        Album("Ring Ring", 1973, 2, 12),
        Album("Red", 2012, 3, 13)
    ]

def test_delete_an_album(db_connection):
    # Given a target album ID
    # It removes the specified row from the albums table.
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    repository.delete(4)
    albums = repository.all()
    assert albums == [
        Album("Doolittle", 1989, 1, 1),
        Album("Surfer Rosa", 1988, 1, 2),
        Album("Waterloo", 1974, 2, 3),
        Album("Bossanova", 1990, 1, 5),
        Album("Lover", 2019, 3, 6),
        Album("Folklore", 2020, 3, 7),
        Album("I Put a Spell on You", 1965, 4, 8),
        Album("Baltimore", 1978, 4, 9),
        Album("Here Comes the Sun", 1971, 4, 10),
        Album("Fodder on My Wings", 1982, 4, 11),
        Album("Ring Ring", 1973, 2, 12)
    ]
