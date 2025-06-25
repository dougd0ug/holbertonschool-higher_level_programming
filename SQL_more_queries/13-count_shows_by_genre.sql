--  lists all shows contained in the database hbtn_0d_tvshows
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_shows
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.genre_id IS NOT NULL
GROUP BY genre
ORDER BY number_shows DESC;
