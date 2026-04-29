import psycopg2
import time
from flask import Flask, render_template, request
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# based on example app.py get_db_connection()
def connectToDatabase():
    connection = psycopg2.connect(
        dbname="Football",
        user="postgres",
        password=os.getenv("YOUR_PASSWORD"),
        host="localhost"
    )

    return connection

# based on example app.py index()
@app.route("/", methods=["GET", "POST"])
def index():
    querySearchResults = []
    executionTimer = None
    queryType = None

    if request.method == "POST":
        queryValue = request.form.get("searchValue")
        queryMode = request.form.get("queryMode")       # indexed vs non-indexed queries
        queryOptions = request.form.get("queryOptions")     # singleQuery queries vs joinedQuery queries

        databaseConnection = connectToDatabase()
        cursor = databaseConnection.cursor()
        
        if queryMode == "indexed":
            cursor.execute("CREATE INDEX IF NOT EXISTS last_name_index ON players(last_name);")
            cursor.execute("CREATE INDEX IF NOT EXISTS player_id_index ON gamestats(player_id);")
        else:
            cursor.execute("DROP INDEX IF EXISTS last_name_index;")
            cursor.execute("DROP INDEX IF EXISTS player_id_index;")

        databaseConnection.commit() # commit index or drop index

        # Define search query based on options
        sqlQueryOnDatabase = ""
        if queryOptions == "singleQuery":
            sqlQueryOnDatabase = """
                SELECT player_id, first_name, last_name, position, hometown 
                FROM players 
                WHERE last_name LIKE %s 
                LIMIT 5;
            """
        else:
            sqlQueryOnDatabase = """
                SELECT p.first_name, p.last_name, gs.date_of_game, gs.stadium_name, gs.points
                FROM players p
                JOIN gamestats gs
                ON p.player_id = gs.player_id
                WHERE p.last_name LIKE %s
                LIMIT 5;
            """
                                    
        # measure query time
        startTime = time.perf_counter()
        #execute query
        cursor.execute(sqlQueryOnDatabase, (f"%{queryValue}%",))
        #retrieve results
        querySearchResults = cursor.fetchall()
        endTime = time.perf_counter()
        executionTimer = (endTime - startTime) * 1000 #execution timer in milliseconds

        cursor.close()
        databaseConnection.close()
    
    return render_template("frontEndQueryTool.html", returnedSearchResults=querySearchResults, executionTime=executionTimer)

if __name__ == "__main__":
    app.run(debug=True)