-- a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT `name`, SUM(`rate`) AS `rating` FROM `tv_genres` AS a
INNER JOIN `tv_show_genres` AS b
ON  a.`id` = b.`genre_id`

INNER JOIN `tv_show_ratings` AS c
ON b.`show_id` = c.`show_id`
GROUP BY `name`
ORDER BY `rating` 
DESC;
