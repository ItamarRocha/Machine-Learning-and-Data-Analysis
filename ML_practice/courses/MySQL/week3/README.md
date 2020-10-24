# Week 3

## Summarizing Data

![](images/data_summarizing.png)

* COUNT

```sql
SELECT COUNT(DISTINCT dog_guid)
FROM complete_tests
WHERE created_at > "2014_03_01"
```

> When a column is included in a count function, null values are ignored in the count. When an asterisk is included in a count function, nulls are included in the count.

https://www.w3resource.com/mysql/mysql-functions-and-operators.php

* ISNULL
```sql
SELECT SUM(ISNULL(exclude))
FROM dogs
```

AVG
MAX
MIN

## Summaries of Groups of Data

* GROUP BY

```sql
SELECT test_name, AVG(rating) AS AVG_Rating
FROM reviews
GROUP BY test_name
```

MySQL allows you to use aliases in a GROUP BY clause, but some database systems do not. If you are using a database system that does NOT accept aliases in GROUP BY clauses, you can still group by derived fields, but you have to duplicate the calculation for the derived field in the GROUP BY clause in addition to including the derived field in the SELECT clause:

```sql
SELECT test_name, MONTH(created_at) AS Month, COUNT(created_at) AS Num_Completed_Tests
FROM complete_tests
GROUP BY test_name, MONTH(created_at);
```

Some database servers, including MySQL, allow you to use numbers in place of field names in the GROUP BY or ORDER BY fields to reduce the overall length of the queries. I tend to avoid this abbreviated method of writing queries because I find it challenging to troubleshoot when you are writing complicated queries with many fields, but it does allow you to write queries faster. To use this method, assign each field in your SELECT statement a number acording to the order the field appears in the SELECT statement. In the following statement:

```sql
SELECT test_name, MONTH(created_at) AS Month, COUNT(created_at) AS Num_Completed_Tests

# test_name would be #1, Month would be #2, and Num_Completed_Tests would be #3. You could then rewrite the query above to read:

SELECT test_name, MONTH(created_at) AS Month, COUNT(created_at) AS Num_Completed_Tests
FROM complete_tests
GROUP BY 1, 2
ORDER BY 1 ASC, 2 ASC;
```

* HAVING

<img src="https://duke.box.com/shared/static/irmwu5o8qcx4ctapjt5h0bs4nsrii1cl.jpg" width=600 alt="ORDER" />

## Joining tables with inner joins

An inner join is a join that outputs only rows that have an exact match in both tables being joined:

<img src="https://duke.box.com/shared/static/xazeqtyq6bjo12ojvgxup4bx0e9qcn5d.jpg" width=400 alt="INNER_JOIN" />


## Left and Right Joins

Left and right joins use a different syntax than we used in the lesson about inner joins.  The method I showed you to execute inner joins tells the database how to relate tables in a WHERE clause like this:

```sql
WHERE d.dog_guid=r.dog_guid
```

I find this syntax -- called the "equijoin" syntax -- to be very intuitive, so I thought it would be a good idea to start with it.  However, we can re-write the inner joins in the same syntax used by outer joins.  To use this more traditional syntax, you have to tell the database how to connect the tables using an ON clause that comes right after the FROM clause.  Make sure to specify the word "JOIN" explicitly.  This traditional version of the syntax frees up the WHERE clause for other things you might want to include in your query.  Here's what one of our queries from the inner join lesson would look like using the traditional syntax:

```mySQL
SELECT d.dog_guid AS DogID, d.user_guid AS UserID, AVG(r.rating) AS AvgRating, COUNT(r.rating) AS NumRatings, d.breed, d.breed_group, d.breed_type
FROM dogs d JOIN reviews r
  ON d.dog_guid=r.dog_guid AND d.user_guid=r.user_guid
GROUP BY d.user_guid
HAVING NumRatings > 9
ORDER BY AvgRating DESC
LIMIT 200
```

You could also write "INNER JOIN" instead of "JOIN" but the default in MySQL is that JOIN will mean inner join, so including the word "INNER" is optional.

If you need a WHERE clause in the query above, it would go after the ON clause and before the GROUP BY clause.

Here's an example of a different query we used in the last lesson that employed the equijoin syntax:

```mySQL
SELECT d.user_guid AS UserID, d.dog_guid AS DogID, 
       d.breed, d.breed_type, d.breed_group
FROM dogs d, complete_tests c
WHERE d.dog_guid=c.dog_guid AND test_name='Yawn Warm-up';
```

**Question 1: How would you re-write this query using the traditional join syntax?**