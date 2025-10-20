
from dotenv import load_dotenv
load_dotenv()  # load environment variables

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google model and generate SQL query from question
def get_gemini_response(question, prompt):
    try:
        model = genai.GenerativeModel('models/gemini-pro-latest')
        #model = genai.GenerativeModel('google-ai-generativelanguage-0.6.15') #('models/text-bison-001')  # Use a valid model name here
        response = model.generate_content([prompt[0], question])
        return response.text
    except Exception as e:
        return f"Error generating response: {e}"

# Function to execute SQL query on SQLite DB and fetch results
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows
    except Exception as e:
        return f"Error executing SQL: {e}"

# Define the Prompt for the model
prompt = ["""   
You are an expert in converting English questions to SQL query!
The SQL database has the name STUDENT and has the following columns NAME, CLASS,
SECTION and MARKS.

For example,
Example 1: How many entries of records are present?
The SQL command will be something like this: SELECT COUNT(*) FROM STUDENT;

Example 2: Tell me all the students studying in Data Science class?
The SQL command will be something like this: SELECT * FROM STUDENT where CLASS="Data Science";

Also, the SQL code should not have ''' in beginning or end and should not include the word 'sql' in the output.
"""]

# Streamlit UI
st.set_page_config(page_title="SQL Query Generator with Gemini/Text-Bison")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input your question:", key="input")
submit = st.button("Ask the question")

if submit:
    with st.spinner("Generating SQL query..."):
        response = get_gemini_response(question, prompt)
    
    # If an error occurred during generation, show error message
    if response.startswith("Error"):
        st.error(response)
    else:
        st.subheader("Generated SQL Query")
        st.code(response)

        # Run the query on student.db
        with st.spinner("Executing SQL query..."):
            data = read_sql_query(response, "student.db")

        if isinstance(data, str) and data.startswith("Error"):
            st.error(data)
        elif data:
            st.subheader("Query Results")
            for row in data:
                st.write(row)
        else:
            st.info("No data found or empty result.")
	