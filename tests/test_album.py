from lib.album import Album

def test_creates_valid_album():
    album = Album("Doolittle", 1989, 1, 1)
    assert album.id == 1
    assert album.title == "Doolittle"
    assert album.release_year == 1989
    assert album.artist_id == 1

def test_outputs_album_data():
    album = Album("Hello", 1991, 3, 4)
    assert str(album) == "4, Hello, 1991, 3"

def test_class_comparison():
    album_1 = Album("Goodbye", 1976, 5, 2)
    album_2 = Album("Goodbye", 1976, 5, 2)
    assert album_1 == album_2