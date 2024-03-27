-- a script that lists all the tables of a database in MySQL server.
USE information_schema;

SELECT TABLE_NAME
FROM TABLES
WHERE TABLE_SCHEMA = ?
