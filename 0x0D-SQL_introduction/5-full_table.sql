-- a script that prints the full description of the table first_table 
-- from the database hbtn_0c_0 in MySQL server.
SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, IS_NULLABLE
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = ? AND TABLE_NAME = 'first_table';
