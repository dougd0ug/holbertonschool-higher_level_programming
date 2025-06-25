--  lists all shows contained in the database hbtn_0d_tvshows
SELECT name FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter' AND tv_genres.id IS NOT NULL
ORDER BY tv_genres.name ASC;
