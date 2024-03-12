-- insert a table into a database, and not print an error 
-- 	if table exists
CREATE TABLE IF NOT EXISTS first_table(
	id INT,
	name VARCHAR(256)
);
