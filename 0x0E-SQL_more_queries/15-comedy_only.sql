-- a script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT a.`title` FROM `tv_shows` AS a
INNER JOIN `tv_show_genres` AS b
ON a.`id` = b.`show_id`

INNER JOIN `tv_genres` AS c
ON c.`id` = b.`genre_id`
WHERE c.`name` = "Comedy"
ORDER BY a.`title`;
