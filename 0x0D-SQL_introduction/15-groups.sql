-- Count the number of records with the same score and display the score along with the count
SELECT score, COUNT(*) AS number
FROM hbtn_0c_0.second_table
GROUP BY score
ORDER BY number DESC;
