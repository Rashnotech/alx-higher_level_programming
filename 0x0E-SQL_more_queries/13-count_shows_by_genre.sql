-- a script that lists all genres
-- displays the number of show linked to each
SELECT tv_genres.name, COUNT(tv_show_genres.genre_id) AS 'number_of_shows'
FROM tv_genres LEFT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
