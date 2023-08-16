-- a script that displays the top 3 of cities
-- temperature during JULY and AUGUST
SELECT city, AVG(value) AS 'avg_temp' FROM temperatures WHERE month BETWEEN 7 AND 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
