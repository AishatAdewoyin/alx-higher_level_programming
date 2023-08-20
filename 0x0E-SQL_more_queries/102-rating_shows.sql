-- a script that lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT `title`, SUM(`rate`) AS `rating` FROM `tv_shows` AS a
INNER JOIN `tv_show_ratings` AS b
ON a.`id` = b.`show_id`
GROUP BY `title`
ORDER BY `rating`
DESC;
