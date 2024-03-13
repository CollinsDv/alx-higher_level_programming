-- lists all records (in score, name order) of second_table where name has to be
-- 	in descending order
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
