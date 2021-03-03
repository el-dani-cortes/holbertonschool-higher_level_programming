-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use a maximum of two SELECT statement
SELECT DISTINCT s.title AS title
FROM tv_shows AS s
WHERE s.title NOT IN
      (SELECT s.title AS title
       FROM tv_genres AS g
       INNER JOIN tv_show_genres AS sg
       ON sg.genre_id = g.id
       INNER JOIN tv_shows AS s
       ON sg.show_id = s.id
       WHERE g.name = "Comedy")
ORDER BY title ASC;
