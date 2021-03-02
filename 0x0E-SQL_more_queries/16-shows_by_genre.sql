-- Lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- If a show doesnt have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT s.title AS title, g.name AS name
FROM tv_genres AS g
INNER JOIN tv_show_genres AS sg
      ON sg.genre_id = g.id
LEFT JOIN tv_shows AS s
      ON sg.show_id = s.id
ORDER BY title ASC, name ASC;
