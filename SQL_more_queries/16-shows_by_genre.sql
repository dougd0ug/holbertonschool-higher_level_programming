--  lists all shows contained in the database hbtn_0d_tvshows
SELECT title, name FROM tv_shows
LEFT JOIN tv_genres ON tv_shows.id = tv_genres.id
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY title, name ASC;
