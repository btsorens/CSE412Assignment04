# CSE 412 Assignment 04
Design and implement a database-backed web application that demonstrates performance difference between search operations executed with and without indexing.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate # or .venv/Scripts/Activate on Windows OS
pip install -r requirements.txt
python ./src/data_generation.py
```

Create a `.env` file in the repo root with:

```
YOUR_PASSWORD=<your postgres user password>
```

Adapted from TPC_H Data into PgAdmin + Sample Queries Doc on Canvas

Step 1: Start PostgreSQL and pgAdmin
1. Ensure PostgresSQL is installed on your system.
2. Open pgAdmin and connect to your Postgre SQL instance.

Step 2: Create the Football Database
1. In pgAdmin, navigate to Servers -> PostgreSQL -> Databases.
2. Right-click on Databases -> Create -> Database...
3. Name the database "Football".
4. Click Save.

Step 3:
1. Open Query Tool in pgAdmin
2. Open and run src/schema.sql:
    * Click File -> Open File -> Select src/schema.sql
    * Click Run 

Data Population
1. Right click on table players -> Import/Export Data
    * Filename ./players.csv
    * Options -> select Header
    * Click OK
2. Right clikc on table gamestats -> Import/Export Data
    * Filename ./gamestats.csv
    * Options -> select Header
    * Click OK
