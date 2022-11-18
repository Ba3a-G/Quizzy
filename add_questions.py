import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

# add questions to db from questions.txt
def add_questions():
    connection = pymysql.connect(
        host=os.getenv('SQL_HOST'),
        user=os.getenv('SQL_USER'),
        password=os.getenv('SQL_PASS'),
        db='quiz_db'
    )
    cursor = connection.cursor()
    with open("questions.txt", "r") as file:
        for line in file:
            parts = line.split(";")
            question = parts[0].strip()
            answer = parts[1].strip()
            options = parts[2].strip()
            command = f"INSERT INTO quiz VALUES ('1', '{question}', '{answer}', '{options}')"
            print(command)
            cursor.execute(command)
    connection.commit()
    connection.close()

if __name__ == "__main__":
    add_questions()