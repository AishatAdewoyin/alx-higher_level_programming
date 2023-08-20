-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download 
-- (same as 11-genre_id_all_shows.sql)
-- Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT a.`title`, b.`genre_id` FROM `tv_shows` AS a
LEFT JOIN `tv_show_genres` AS b
ON a.`id` = b.`show_id`
WHERE b.`genre_id` IS NULL
ORDER BY a.`title`, b.`genre_id`;
