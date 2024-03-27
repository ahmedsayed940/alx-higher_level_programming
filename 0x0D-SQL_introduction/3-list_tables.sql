-- a script that lists all the tables of a database in MySQL server.
SELECT TABLE_NAME
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = ?;
