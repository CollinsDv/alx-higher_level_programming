-- add a database and user if they don't exist
-- database field :
-- 	id is unique, not null and auto-genereted
--	name should not be NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
	);
