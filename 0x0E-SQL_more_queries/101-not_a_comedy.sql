-- a script that lists all shows without the genre
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (SELECT tv_genres.id
	FROM tv_genres JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
	WHERE tv_genres.name = 'Comedy')
ORDER BY tv_shows.title ASC;
