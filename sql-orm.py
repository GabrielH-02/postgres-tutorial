from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions form the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Artist" table
class artist(base):
    __tablename__ = "artist"
    artist_id = Column(Integer, primary_key=True)
    name = Column(String)


# create a class-based model for the "Album" table
class album(base):
    __tablename__ = "album"
    album_id = Column(Integer, primary_key=True)
    title = Column(String)
    artist_id = Column(Integer, ForeignKey("artist.artist_id"))


# create a class-based model for the "Track" table
class track(base):
    __tablename__ = "track"
    track_id = Column(Integer, primary_key=True)
    name = Column(String)
    album_id = Column(Integer, ForeignKey("album.qlbum_id"))
    media_type_id = Column(Integer, primary_key=False)
    genre_id = Column(Integer, primary_key=False)
    composer =  Column(String)
    milliseconds = Column(Integer, primary_key=False)
    bytes = Column(Integer, primary_key=False)
    unit_price = Column(Float)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)



# Query 1 - select all records from the "Artist" table
# artistts = session.query(artist)
# for artistt in artistts:
#     print(artistt.artist_id, artistt.name, sep=" | ")

# Query 2 - select only the "Name" column from the "Artist" table
# artistts = session.query(artist)
# for artistt in artistts:
#     print(artistt.name)

# Query 3 - select only 'Queen' from the "Artist" table
# artisto = session.query(artist).filter_by(name='Queen').first()
# print(artisto.artist_id, artisto.name, sep=" | ")

# Query 4 - select only by 'ArtistId' #51 from the "Artist" table
# artisto = session.query(artist).filter_by(artist_id=51).first()
# print(artisto.artist_id, artisto.name, sep=" | ")

# Query 5 - select only the albums with 'ArtistId' #51 on the "Album" table
# albumms = session.query(album).filter_by(artist_id=51)
# for albumm in albumms:
#     print(albumm.album_id, albumm.title, albumm.artist_id, sep=" | ")

# Query 6 - select all tracks where the composer is 'Queen' from the "Track" table
# trackks = session.query(track).filter_by(composer='Queen')
# for trackk in trackks:
#     print(
#         trackk.track_id,
#         trackk.name,
#         trackk.album_id,
#         trackk.media_type_id,
#         trackk.genre_id,
#         trackk.composer,
#         trackk.milliseconds,
#         trackk.bytes,
#         trackk.unit_price,
#         sep=" | "
#     )
