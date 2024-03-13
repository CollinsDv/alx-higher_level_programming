-- creates a table in a database and shouldn't raise an error
-- if it exists. Database will be passed as cmd arguement
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
);
