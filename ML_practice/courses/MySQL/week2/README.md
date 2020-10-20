# Week 2

## Queries

> Query:
SQL code that describes the data you desire and the format in which you want it

* All queries start with a verb SELECT followed by clauses that identify the data and the database you want to work with and the format.

![images/order.png](images/order.png)

* SELECT and from and required
* You must end your queries with ;

## Syntax

* Recommended syntax is to write each keyword along with the caracthers that follow them in each line as :

![](images/syntax.png)

## Other Keywords/Commands

* SHOW

Examples:
```SQL
SHOW tables
SHOW columns FROM $table$
SHOW columns FROM $table$ FROM $database$
SHOW columns FROM $databasename.tablename$
```

* DESCRIBE

> Gets a detailed description of the table

<table>
    <tbody>
        <tr>
            <th>Field</th>
            <th>Type</th>
            <th>Null</th>
            <th>Key</th>
            <th>Default</th>
            <th>Extra</th>
        </tr>
        <tr>
            <td>created_at</td>
            <td>datetime</td>
            <td>NO</td>
            <td></td>
            <td>None</td>
            <td></td>
        </tr>
        <tr>
            <td>updated_at</td>
            <td>datetime</td>
            <td>NO</td>
            <td></td>
            <td>None</td>
            <td></td>
        </tr>
        <tr>
            <td>user_guid</td>
            <td>varchar(60)</td>
            <td>YES</td>
            <td>MUL</td>
            <td>None</td>
            <td></td>
        </tr>
        <tr>
            <td>dog_guid</td>
            <td>varchar(60)</td>
            <td>YES</td>
            <td>MUL</td>
            <td>None</td>
            <td></td>
        </tr>
        <tr>
            <td>test_name</td>
            <td>varchar(60)</td>
            <td>YES</td>
            <td></td>
            <td>None</td>
            <td></td>
        </tr>
        <tr>
            <td>subcategory_name</td>
            <td>varchar(60)</td>
            <td>YES</td>
            <td></td>
            <td>None</td>
            <td></td>
        </tr>
    </tbody>
</table>

* SQL syntax and keywords are case insensitive. I recommend that you always enter SQL keywords in upper case and table or column names in either lower case or their native format to make it easy to read and troubleshoot your code, but it is not a requirement to do so. Table or column names are often case insensitive as well, but defaults may vary across database platforms so it's always a good idea to check.
* Table or column names with spaces in them need to be surrounded by quotation marks in SQL. MySQL accepts both double and single quotation marks, but some database systems only accept single quotation marks. In all database systems, if a table or column name contains an SQL keyword, the name must be enclosed in backticks instead of quotation marks.

>    'the marks that surrounds this phrase are single quotation marks'
    "the marks that surrounds this phrase are double quotation marks"
    \`the marks that surround this phrase are backticks\`


* The semi-colon at the end of a query is only required when you have multiple separate queries saved in the same text file or editor. That said, I recommend that you make it a habit to always include a semi-colon at the end of your queries. 

* LIMIT

Limitates the number of rows selected

* OFFSET

Give a offset to the SELECT clause

```SQL
SELECT breed
FROM dogs LIMIT 10 OFFSET 5;
```

or you could just do:

```SQL
SELECT breed
FROM dogs LIMIT 5,10;
```
## SQL function and operators

https://dev.mysql.com/doc/refman/5.7/en/sql-function-reference.html

https://www.w3resource.com/mysql/mysql-functions-and-operators.php

* IN operator

Lets you select more than one string value

```SQL
SELECT dog_guid, breed
FROM dogs
WHERE breed IN ("golden retriever","poodle");
```

* LIKE operator

The LIKE operator allows you to specify a pattern that the textual data you query has to match. For example, if you wanted to look at all the data from breeds whose names started with "s", you could query:

```SQL
SELECT dog_guid, breed
FROM dogs
WHERE breed LIKE ("s%");
```

In this syntax, the percent sign indicates a wild card. Wild cards represent unlimited numbers of missing letters. This is how the placement of the percent sign would affect the results of the query:

* WHERE breed LIKE ("s%") = the breed must start with "s", but can have any number of letters after the "s"
* WHERE breed LIKE ("%s") = the breed must end with "s", but can have any number of letters before the "s"
* WHERE breed LIKE ("%s%") = the breed must contain an "s" somewhere in its name, but can have any number of letters before or after the "s"

## Time 

https://www.tutorialspoint.com/mysql/mysql-date-time-functions.htm

