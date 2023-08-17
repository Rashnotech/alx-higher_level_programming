-- a script that lists all the cities found in dbase
-- ;
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name LIKE 'California') ORDER BY cities.id ASC;

