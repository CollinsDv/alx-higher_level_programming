-- create a database and a user(with a password) and grant SELECT privilege to user
-- on the database. Shouldn't fail if database or user exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

GRANT SELECT
ON hbtn_0d_2.*
TO 'user_0d_2'@'localhost';
