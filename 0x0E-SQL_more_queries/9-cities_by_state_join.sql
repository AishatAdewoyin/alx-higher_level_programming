-- a script that lists all cities contained in the database hbtn_0d_usa.
SELECT a.`id`, a.`name`, b.`name` FROM `cities` AS a
INNER JOIN `states` AS b
ON a.`state_id` = b.`id`
ORDER BY a.`id`;
