--a script that creates the database hbtn_0d_2 and the user user_0d_2.
-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create or update the user and set the password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Set privileges for the user only if the user exists
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
