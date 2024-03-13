-- lists records in a table  in score, name order
--	and ordered by score max value
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
