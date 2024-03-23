from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create variable from "artist" table
artist_table = Table(
    "artist", meta,
    Column("artist_id", Integer, primary_key=True),
    Column("name", String)
)

# create variable for "album" table
album_table = Table(
    "album", meta, 
    Column("album_id", Integer, primary_key=True),
    Column("Title", String),
    Column("artist_id", Integer, ForeignKey("artist_table.artist_id"))
)

# create variable for "track" table
track_table = Table(
    "track", meta,
    Column("track_id", Integer, primary_key=True),
    Column("name", String),
    Column("album_id", Integer, ForeignKey("album_table.album_id")),
    Column("media_type_id", Integer, primary_key=False),
    Column("genre_id", Integer, primary_key=False),
    Column("composer", String),
    Column("milliseconds", Integer),
    Column("bytes", Integer),
    Column("unit_price", Float)
)

# making the connection
with db.connect() as connection:

    # Query 1 - select all records from the ""artist table
    select_query = artist_table.select()

    results = connection.execute(select_query)
    for result in results:
        print(result)
