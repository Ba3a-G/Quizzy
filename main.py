import pymysql
import random
from dotenv import load_dotenv
import os

load_dotenv()

# Connect to the database and load questions
def load_questions():
    connection = pymysql.connect(
        host=os.getenv('SQL_HOST'),
        user=os.getenv('SQL_USER'),
        password=os.getenv('SQL_PASS'),
        db='quiz_db'
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM quiz")
    questions = cursor.fetchall()
    connection.close()
    return questions

# Pick a random question
def ask(questions):
    question = random.choice(questions)
    print(question[1])
    print("1. " + question[3].split(",")[0].strip())
    print("2. " + question[3].split(",")[1].strip())

    answer = input("Enter your answer: ").lower()
    if answer == question[2].lower():
        print("Correct!")
    else:
        print("Wrong!")

if __name__ == "__main__":
    questions = load_questions()
    print(questions)
    while True:
        ask(questions)
        print("Do you want to continue? (y/n)")
        answer = input().lower()
        if answer == "n":
            break