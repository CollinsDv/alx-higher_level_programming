-- creates a table in a database and shouldn't raise an error
-- if it exists. Database will be passed as cmd arguement
-- Id field has a default value
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
);
