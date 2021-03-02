-- Uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT s.title AS title
FROM tv_genres AS g
INNER JOIN tv_show_genres AS sg
      ON sg.genre_id = g.id
INNER JOIN tv_shows AS s
      ON sg.show_id = s.id
WHERE g.name = "Comedy"
ORDER BY title ASC;
