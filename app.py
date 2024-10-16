from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure GenAI Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Google Gemini
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    # Extract response text
    if hasattr(response, 'text'):
        return response.text
    else:
        st.error("Failed to generate a valid response from the Gemini model.")
        return ""

# Function to read SQL query from database
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows
    except sqlite3.OperationalError as e:
        print(f"An error occurred: {e}")
        return []

# Update prompt with columns
prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION, MARKS.
    For example:
    Example 1 - How many entries of records are present?, the SQL command will be:
    SELECT COUNT(*) FROM STUDENT;
    Example 2 - Tell me all the students studying in Data Science class?, the SQL command will be:
    SELECT * FROM STUDENT WHERE CLASS="Data Science";
    Also, the SQL code should not include any formatting symbols like ``` or have the keyword "sql" in the output.
    """
]

# Streamlit App Configuration
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

# Get user input
question = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

# When submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    st.write(f"Generated SQL Query: {response}")  # Display the generated SQL query for verification
    if response:
        rows = read_sql_query(response, "student.db")
        if rows:
            st.subheader("The Response is")
            for row in rows:
                st.write(row)
        else:
            st.write("No results found or an error occurred.")
