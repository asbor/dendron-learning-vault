---
id: knowledge.sql.sql-statements
title: SQL Statements
desc: "SQL tutorial and reference"
updated: 1761144402000
created: 1761144402000
---


SQL stands for Structured Query Language. It is a standard language for accessing and manipulating databases. SQL is used to communicate with a database. According to ANSI (American National Standards Institute), it is the standard language for relational database management systems. SQL statements are used to perform tasks such as update data on a database, or retrieve data from a database. Some common relational database management systems that use SQL are: Oracle, Sybase, Microsoft SQL Server, Access, Ingres, etc. Although most database systems use SQL, most of them also have their own additional proprietary extensions that are usually only used on their system.

## SQL Statements

### `SELECT` Statement

The SELECT statement is used to select **data** from a **database**. The **data** returned is stored in a **result table**, called the **result-set**.

```sql
SELECT column1, column2, ...
FROM table_name;
```

### `SELECT DISTINCT` Statement

The `SELECT DISTINCT` statement is used to return only distinct (different) values. Inside a table, a column often contains many duplicate values; and sometimes you only want to list the different (distinct) values.

```sql
SELECT DISTINCT column1, column2, ...
FROM table_name;
```

### `WHERE` Clause

The `WHERE` clause is used to extract only those records that fulfill a specified condition.

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

### `AND` Operator

The `AND` operator is used to filter records based on more than one condition.

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2;
```

### `OR` Operator

The `OR` operator is used to filter records based on more than one condition.

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition1 OR condition2;
```

### `ORDER BY` Keyword

The `ORDER BY` keyword is used to sort the result-set in ascending or descending order.

```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;
```

### `INSERT INTO` Statement

The `INSERT INTO` statement is used to insert new records in a table.

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

### `UPDATE` Statement

The `UPDATE` statement is used to modify the existing records in a table.

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

### `DELETE` Statement

The `DELETE` statement is used to delete existing records in a table.

```sql
DELETE FROM table_name
WHERE condition;
```

### `CREATE DATABASE` Statement

The `CREATE DATABASE` statement is used to create a new SQL database.

```sql
CREATE DATABASE database_name;
```

### `DROP DATABASE` Statement

The `DROP DATABASE` statement is used to delete a SQL database.

```sql
DROP DATABASE database_name;
```

### `CREATE TABLE` Statement

The `CREATE TABLE` statement is used to create a new table in a database.

```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
    ...
);
```

### `DROP TABLE` Statement

The `DROP TABLE` statement is used to delete a table in a database.

```sql
DROP TABLE table_name;
```

### `ALTER TABLE` Statement

The `ALTER TABLE` statement is used to add, delete, or modify columns in an existing table.

```sql
ALTER TABLE table_name
ADD column_name datatype;
```

### `CREATE INDEX` Statement

The `CREATE INDEX` statement is used to create an index in a table.

```sql
CREATE INDEX index_name
ON table_name (column1, column2, ...);
```

### `DROP INDEX` Statement

The `DROP INDEX` statement is used to delete an index in a table.

```sql
DROP INDEX table_name.index_name;
```

### `GROUP BY` Statement

The `GROUP BY` statement is used in conjunction with the `SELECT` statement to arrange identical data into groups.

```sql
SELECT column1, column2, ...
FROM table_name
GROUP BY column1, column2, ...
```

### `HAVING` Clause

The `HAVING` clause was added to SQL because the `WHERE` keyword could not be used with aggregate functions.

```sql
SELECT column1, column2, ...
FROM table_name
GROUP BY column1, column2
HAVING condition;
```

### `JOIN` Statement

A `JOIN` clause is used to combine rows from two or more tables, based on a related column between them.

```sql
SELECT column_name(s)
FROM table1
JOIN table2
ON table1.column_name = table2.column_name;
```

### `UNION` Operator

The `UNION` operator is used to combine the result-set of two or more `SELECT` statements.

```sql
SELECT column1, column2, ...
FROM table1
UNION
SELECT column1, column2, ...
FROM table2;
```

### `UNION ALL` Operator

The `UNION ALL` operator is used to combine the result-set of two or more `SELECT` statements.

```sql
SELECT column1, column2, ...
FROM table1
UNION ALL
SELECT column1, column2, ...
FROM table2;
```

The difference between `UNION` and `UNION ALL` is that `UNION` selects only distinct values, while `UNION ALL` selects all values.

### `EXISTS` Operator

The `EXISTS` operator is used to test for the existence of any record in a subquery.

```sql
SELECT column1, column2, ...
FROM table_name
WHERE EXISTS (SELECT column1 FROM table_name WHERE condition);
```

### `ANY` Operator

The `ANY` operator is used to compare a value to any applicable value in the list according to the condition.

```sql
SELECT column1, column2, ...
FROM table_name
WHERE column_name operator ANY (SELECT column_name FROM table_name WHERE condition);
```

### `ALL` Operator

The `ALL` operator is used to compare a value to all applicable values in the list according to the condition.

```sql
SELECT column1, column2, ...
FROM table_name
WHERE column_name operator ALL (SELECT column_name FROM table_name WHERE condition);
```

### `BETWEEN` Operator

The `BETWEEN` operator selects values within a given range.

```sql
SELECT column1, column2, ...
FROM table_name
WHERE column_name BETWEEN value1 AND value2;
```

### `LIKE` Operator

The `LIKE` operator is used in a `WHERE` clause to search for a specified pattern in a column.

```sql
SELECT column1, column2, ...
FROM table_name
WHERE column_name LIKE pattern;
```

### `IN` Operator

The `IN` operator allows you to specify multiple values in a `WHERE` clause.

```sql
SELECT column1, column2, ...
FROM table_name
WHERE column_name IN (value1, value2, ...);
```

### `IS NULL` Operator

The `IS NULL` operator is used to test for empty values (NULL values).

```sql
SELECT column1, column2, ...
FROM table_name
WHERE column_name IS NULL;
```

### `IS NOT NULL` Operator

The `IS NOT NULL` operator is used to test for empty values (NULL values).

```sql
SELECT column1, column2, ...
FROM table_name
WHERE column_name IS NOT NULL;
```

### `CREATE VIEW` Statement

The `CREATE VIEW` statement is used to create a virtual table based on the result-set of an SQL statement.

```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

### `DROP VIEW` Statement

The `DROP VIEW` statement is used to delete a view.

```sql
DROP VIEW view_name;
```

### `TRUNCATE TABLE` Statement

The `TRUNCATE TABLE` statement is used to delete the data inside a table, but not the table itself.

```sql
TRUNCATE TABLE table_name;
```

### `RENAME TABLE` Statement

The `RENAME TABLE` statement is used to rename an existing table.

```sql
RENAME TABLE table_name TO new_table_name;
```

### `CREATE PROCEDURE` Statement

The `CREATE PROCEDURE` statement is used to create a stored procedure.

```sql
CREATE PROCEDURE procedure_name
AS
sql_statement
```

### `DROP PROCEDURE` Statement

The `DROP PROCEDURE` statement is used to delete a stored procedure.

```sql
DROP PROCEDURE procedure_name;
```

### `CREATE FUNCTION` Statement

The `CREATE FUNCTION` statement is used to create a user-defined function.

```sql
CREATE FUNCTION function_name
AS
sql_statement
```

The difference between a function and a stored procedure is that a function returns a value, while a stored procedure does not.

### `DROP FUNCTION` Statement

The `DROP FUNCTION` statement is used to delete a user-defined function.

```sql
DROP FUNCTION function_name;
```

### `CREATE TRIGGER` Statement

The `CREATE TRIGGER` statement is used to create a trigger.

```sql
CREATE TRIGGER trigger_name
AFTER INSERT
ON table_name
FOR EACH ROW
BEGIN
sql_statement;
END;
```

### `DROP TRIGGER` Statement

The `DROP TRIGGER` statement is used to delete a trigger.

```sql
DROP TRIGGER trigger_name;
```

### `CREATE SCHEMA` Statement

The `CREATE SCHEMA` statement is used to create a new schema in a database.

```sql
CREATE SCHEMA schema_name;
```

### `DROP SCHEMA` Statement

The `DROP SCHEMA` statement is used to delete a schema in a database.

```sql
DROP SCHEMA schema_name;
```

### `GRANT` Statement

The `GRANT` statement is used to give privileges to a user.

```sql
GRANT privilege_name
ON object_name
TO user_name;
```

### `REVOKE` Statement

The `REVOKE` statement is used to take back privileges from a user.

```sql
REVOKE privilege_name
ON object_name
FROM user_name;
```

### `COMMIT` Statement

The `COMMIT` statement is used to save the changes made by the transaction.

```sql
COMMIT;
```

### `ROLLBACK` Statement

The `ROLLBACK` statement is used to undo transactions that have not already been saved.

```sql
ROLLBACK;
```

### `SAVEPOINT` Statement

The `SAVEPOINT` statement is used to set a savepoint within a transaction.

```sql
SAVEPOINT savepoint_name;
```

### `ROLLBACK TO SAVEPOINT` Statement

The `ROLLBACK TO SAVEPOINT` statement is used to roll back to a savepoint within a transaction.

```sql
ROLLBACK TO SAVEPOINT savepoint_name;
```

### `SET TRANSACTION` Statement

The `SET TRANSACTION` statement is used to start a new transaction.

```sql
SET TRANSACTION;
```

### `ALTER DATABASE` Statement

The `ALTER DATABASE` statement is used to modify a database.

```sql
ALTER DATABASE database_name
SET parameter_name value;
```

### `ALTER INDEX` Statement

The `ALTER INDEX` statement is used to modify an index.

```sql
ALTER INDEX index_name
ON table_name REBUILD;
```
