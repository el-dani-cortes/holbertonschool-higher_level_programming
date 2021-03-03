-- Script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT DISTINCT g.name AS name
FROM tv_genres AS g
INNER JOIN tv_show_genres AS sg
      ON sg.genre_id = g.id
WHERE sg.genre_id NOT IN
      (SELECT sg.genre_id
       FROM tv_show_genres AS sg
       INNER JOIN tv_shows AS s
       ON sg.show_id = s.id
       WHERE s.title = "DEXTER")
ORDER BY name ASC;
