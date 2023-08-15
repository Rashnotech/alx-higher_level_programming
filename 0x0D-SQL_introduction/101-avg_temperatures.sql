-- a script that displays the average temperature
-- (Fahrenheit) by city ordered by temperature (descending)
SELECT city, AVG((value * 1.8) + 32) AS 'avg_temp' FROM temperatures ORDER BY avg_temp DESC;

