import psycopg2
import time
from flask import Flask, render_template, request

app = Flask(__name__)

def connectToDatabase():
    connection = psycopg2.connect(
        dbname="brocks_database",
        user="fasta",
        password="PASSWORD",
        host="localhost"
    )

    return connection