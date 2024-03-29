-- Count the number of records with the same score and display the score along with the count
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
