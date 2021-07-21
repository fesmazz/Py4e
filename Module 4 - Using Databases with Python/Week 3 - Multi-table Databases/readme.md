# Musical Track Database
This application will read an iTunes export file in XML and produce a properly normalized database with this structure:

>CREATE TABLE Artist \( \n
>    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, \n
>    name    TEXT UNIQUE \n
>\); \n
>
>CREATE TABLE Genre \( \n
>    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, \n
>    name    TEXT UNIQUE \n
>\); \n
>
>CREATE TABLE Album \( \n
>    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, \n
>    artist_id  INTEGER, \n
>    title   TEXT UNIQUE \n
>\); \n
>
>CREATE TABLE Track \( \n
>    id  INTEGER NOT NULL PRIMARY KEY \n 
>        AUTOINCREMENT UNIQUE, \n
>    title TEXT  UNIQUE, \n
>    album_id  INTEGER, \n
>    genre_id  INTEGER, \n
>    len INTEGER, rating INTEGER, count INTEGER \n
>\); \n

If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.py4e.com/code3/tracks.zip. The ZIP file contains the Library.xml file to be used for this assignment. You can export your own tracks from iTunes and create a database, but for the database that you turn in for this assignment, only use the Library.xml data that is provided.

To grade this assignment, the program will run a query like this on your uploaded database and look for the data it expects to see:

>SELECT Track.title, Artist.name, Album.title, Genre.name \n
>    FROM Track JOIN Genre JOIN Album JOIN Artist \n
>    ON Track.genre_id = Genre.ID and Track.album_id = Album.id \n
>        AND Album.artist_id = Artist.id \n
>    ORDER BY Artist.name LIMIT 3 \n