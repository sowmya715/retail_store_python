"""
Problem Statement:
Write a Python program that connects to a SQLite database (sample.db) and 
answers several questions by executing SQL queries. After retrieving results, 
insert new data into the Playlist and PlaylistTrack tables.

Requirements:
1. Connect to the database sample.db using sqlite3.
2. Retrieve:
   - The artist that has an ArtistId of 253.
   - All album titles for the artist "Yo-Yo Ma".
   - The longest track in the database (track with the maximum milliseconds).
   - The number of tracks in the genre "Latin".
   - A count of tracks for each genre, ordered from most to fewest.

3. Insert new data:
   - Add a new playlist named "AMERICAN BAND" into the Playlist table.
   - Retrieve the playlist id of the newly inserted playlist.
   - Insert three tracks (TrackIds: 200, 300, 400) into PlaylistTrack 
     using this playlist id.

4. Commit all changes and close the database connection.

Database Assumptions:
- Database file is named sample.db.
- Tables used:
    Artist(ArtistId, Name)
    Album(AlbumId, Title, ArtistId)
    Track(TrackId, Name, Milliseconds, GenreId)
    Genre(GenreId, Name)
    Playlist(PlaylistId, Name)
    PlaylistTrack(PlaylistId, TrackId)

Output:
- Print results for all SELECT queries.
- Print confirmation messages after inserting playlist and tracks.
"""


import sqlite3

con = sqlite3.connect("sample.db")
cur = con.cursor()

artist = cur.execute("""SELECT * FROM Artist WHERE ArtistId = 253""")
print("Which artist has an id of 253?", list(artist))

artist_name = cur.execute("""
SELECT Title 
FROM Album AS album
INNER JOIN Artist artist ON artist.ArtistId = album.ArtistId
WHERE artist.Name = "Yo-Yo Ma"
""")
print("List all albums for artist Yo-Yo Ma.", list(artist_name))

longest_track = cur.execute("""
SELECT Name AS NAME, Milliseconds AS MILLISECONDS 
FROM Track 
ORDER BY MILLISECONDS DESC 
LIMIT 1
""")
print("What is the longest track?", list(longest_track))

genre_tracks = cur.execute("""
SELECT COUNT(*) 
FROM Track AS track
INNER JOIN Genre genre ON genre.GenreId = track.GenreId
WHERE genre.Name = "Latin"
""")
print("How many tracks in the Latin genre are there?", list(genre_tracks))

ordered_genre = cur.execute("""
SELECT genre.Name AS GENRENAME, COUNT(*) AS TRACKCOUNT
FROM Track AS track
INNER JOIN Genre genre ON genre.GenreId = track.GenreId
GROUP BY genre.Name
ORDER BY TRACKCOUNT DESC
""")
print("How many tracks for all genres ordered from most to fewest?", list(ordered_genre))

cur.execute("""INSERT INTO Playlist (Name) VALUES ("AMERICAN BAND")""")
con.commit()
print("Playlist added")

playlist_id = cur.lastrowid

cur.execute(f"""INSERT INTO PlaylistTrack VALUES({playlist_id}, 200)""")
cur.execute(f"""INSERT INTO PlaylistTrack VALUES({playlist_id}, 300)""")
cur.execute(f"""INSERT INTO PlaylistTrack VALUES({playlist_id}, 400)""")
print("Tracks Added to playlist")

con.commit()
con.close()
