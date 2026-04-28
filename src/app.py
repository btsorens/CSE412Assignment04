import psycopg2
import time
from flask import Flask, render_template, request

app = Flask(__name__)

# based on example app.py get_db_connection()
def connectToDatabase():
    connection = psycopg2.connect(
        dbname="brocks_database",
        user="fasta",
        password="PASSWORD",
        host="localhost"
    )

    return connection

# based on example app.py index()
@app.route("/", methods=["GET", "POST"])
def index():
    querySearchResults = []
    executionTimer = None

    if request.method == "POST":
        queryValue = request.form.get("searchValue")
        queryMode = request.form.get("queryMode")       # indexed vs non-indexed queries
        queryOptions = request.form.get("queryOptions")     # singleQuery queries vs joinedQuery queries

        databaseConnection = connectToDatabase()
        cursor = databaseConnection.cursor()
        
        if queryMode == "indexed":
            cursor.execute("CREATE INDEX IF NOT EXISTS column_index ON relation(column);")
        
        else:
            cursor.execute("DROP INDEX IF EXISTS column_index;")

        # Define search query based on options
        sqlQueryOnDatabase = ""
        if queryOptions == "singleQuery":
            sqlQueryOnDatabase = "SELECT * FROM relation WHERE column=***"
        else:
            sqlQueryOnDatabase =    """
                                    SELECT r1.column, r2.column
                                    FROM relation1 r1
                                    JOIN relation2 r2
                                    ON r1.id = r2.fid
                                    WHERE r1.column = ***
                                    """
                                    
        cursor.execute(sqlQueryOnDatabase, (f"%{queryValue}%",))
        queryResults = cursor.fetchall()

        cursor.close()
        databaseConnection.close()
    
    return render_template("frontEndQueryTool.html", returnedSearchResults=querySearchResults, executionTime=executionTimer)