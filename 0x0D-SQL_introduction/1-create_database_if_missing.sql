-- creates a database and restricts output if it already exists
IF NOT EXISTS (
	SELECT name FROM master.sys.databases
	WHERE name = N'hbtn_0c_0'
)
BEGIN
	CREATE DATABASE hbtn_0c_0;
END;
