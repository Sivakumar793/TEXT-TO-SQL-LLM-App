SQL Query Generator using Gemini (Google Generative AI)

This project is a Streamlit web app that converts natural language questions into SQL queries using Google’s Gemini API and executes them on a SQLite database.

It allows users to type in English questions (e.g., “Show me all students in Data Science class”) and automatically generates and runs the corresponding SQL query on the local database.

🚀 Features

💬 Convert English questions into SQL queries using Gemini API

🧩 Execute generated SQL queries on a SQLite database (student.db)

📊 Display query results interactively in a Streamlit UI

⚡ Simple and lightweight — runs locally with minimal setup

🧱 Project Structure
.
├── app.py               # Main Streamlit app
├── sql.py               # Script to create and populate SQLite database
├── student.db           # SQLite database (auto-created by sql.py)
├── .env                 # Contains your Gemini API key
├── requirements.txt     # Dependencies
└── README.md            # Project documentation


1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Set Up Environment Variables

Create a file named .env in the project root and add your Gemini API key:

GOOGLE_API_KEY="YOUR_API_KEY_HERE"

🗃️ Database Setup

Run sql.py once to create and populate the database:

python sql.py


This creates a student.db file with sample records:

NAME	CLASS	SECTION	MARKS
Krish	Data Science	A	90
Sudhanshu	Data Science	B	100
Darius	Data Science	A	86
Vikash	DEVOPS	A	50
Dipesh	DEVOPS	A	35
🧠 Run the Streamlit App

Start the Streamlit application:

streamlit run app.py


Then it will open your browser at:

http://localhost:8501/


💡 Example Queries
English Question	Generated SQL Query
How many entries of records are present?	SELECT COUNT(*) FROM STUDENT;
Tell me all the students studying in Data Science class?	SELECT * FROM STUDENT WHERE CLASS="Data Science";
Who scored more than 80 marks?	SELECT * FROM STUDENT WHERE MARKS > 80;
⚙️ Technologies Used

Python 3.10+

Streamlit – Interactive web app framework

SQLite3 – Local database for demo

Google Generative AI (Gemini) – For natural language → SQL generation

dotenv – For secure API key management

🧾 Requirements

All dependencies are listed in requirements.txt:

streamlit
google-generativeai
python-dotenv


Install them using:

pip install -r requirements.txt

🧑‍💻 Author

Siva Kumar M
