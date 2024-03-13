-- creates a table in a database and shouldn't raise an error
-- if it exists. Database will be passed as cmd arguement
-- Id field has a default value and should be uniquee
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
