-- a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT DISTINCT `title` FROM `tv_shows` AS a
LEFT JOIN `tv_show_genres` AS b
ON b.`show_id` = a.`id`

LEFT JOIN `tv_genres` AS c
ON c.`id` = b.`genre_id`
WHERE a.`title` NOT IN
    (SELECT `title` FROM `tv_shows` AS a
	INNER JOIN `tv_show_genres` AS b
	ON b.`show_id` = a.`id`
	INNER JOIN `tv_genres` AS c
	ON c.`id` = b.`genre_id`
	WHERE c.`name` = "Comedy")
ORDER BY `title`;
