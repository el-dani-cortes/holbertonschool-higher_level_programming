-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT shows.title, genres.genre_id
FROM tv_shows AS shows
INNER JOIN tv_show_genres AS genres
ON genres.show_id = shows.id
ORDER BY shows.title ASC, genres.genre_id ASC;
