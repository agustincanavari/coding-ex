## Commit test 1

## Introduction

While you could accomplish some of these tasks using libraries like Pandas or Requests, one of the objectives of this exercise is to evaluate your ability to implement with Python’s standard library. Therefore, it is preferred that you use the “batteries that are included” with Python.


> __HINT :__ You should create new feature branch and clone this repo locally. You will then use your feature branch to submit a PR (pull request) against `dev` at the end of the exercise to present your masterpiece !


### 1. Read CSV files via HTTP and write as JSON

There are two files to be downloaded and transformed:

 - https://pbryan.github.io/exercise/companies.csv
 - https://pbryan.github.io/exercise/opportunities.csv

The `companies` schema:
```
id: universally unique identifier
name: string
start_date: date
logo_image_url: string
employees: integer
target_account: enumeration: Yes, No
```

The `opportunities` schema:
```
id: universally unique identifier
company_id: reference to companies record
amount: integer
type: enumeration: new_logo, expansion, other
updated_at: timestamp in ISO 8601 format
status: enumeration: pending, active, closed
```

Read these CSV files via HTTP, and write them as line-delimited JSON files. Ignore all fields beginning with underscore. Where possible, data should be converted to JSON native types (e.g. numbers, boolean).


### 2. Read JSON files into Python objects

From the files written in [step 1](#1-read-csv-files-via-http-and-write-as-json), read all JSON objects into collections of Python objects in memory. Fields should be accessible as attributes. Where possible, data should be converted into Python native types.

Store collections of companies and opportunities such that each can be efficiently accessed randomly by their primary and foreign keys (if applicable), aiming for *O(1) average time complexity*.


### 3. Generate company report

From all data loaded into objects in memory, output a CSV file, containing:

 - company name
 - start date in mm/dd/yyyy format
 - total amount of opportunities
 - average opportunity amount
 - date of last opportunity update in mm/dd/yyyy format

### 4. Generate summary report

From all data loaded into objects in memory, output a CSV file that summarizes for target accounts and non-target accounts:

 - total opportunity amount
 - average opportunity amount


### 5. Define SQL tables and queries

For the schemas above, define SQL tables, indexes, constraints, etc. that would be appropriate to handle millions of rows of data.

For the reports above, define the SQL queries that would generate similar results. It is not necessary to generate dates in any particular format, nor output in CSV.


### 6. For discussion

 * Explain how you would test the efficiency of the SQL queries you wrote.

 * Explain how, if a SQL query was found to be inefficient, you would go about improving its performance.

 * Explain how typical SQL indexes work.

 * Explain the potential unintended consequences of adding an index to a table.

 * Explain what steps could you take to improve the performance of a one-time import of millions of rows.

 * Explain the differences between INNER JOIN, OUTER LEFT JOIN and OUTER RIGHT JOIN.

 * Explain whether SQL should enforce foreign key constraints, benefits and drawbacks.

 * Explain advantages and disadvantages of SQL vs. key-value databases.
