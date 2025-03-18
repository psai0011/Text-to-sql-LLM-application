from dotenv import load_dotenv
load_dotenv()  # Load all environment variables

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load the Google Gemini Model and provide query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content([prompt[0], question])
    return response

# Function to retrieve the query from the SQL database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)  
    cur = conn.cursor() 

    cur.execute(sql) 
    rows = cur.fetchall()  # Fetch all results

    conn.close() 

    for row in rows:
        print(row)  
    return rows  

# Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION and MARKS 

    For example,

    Example 1 - How many entries of records are present
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;

    Example 2 - Tell me all the students studying in Data Science class?
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science";
    
    Also, the SQL code should not have ... in the beginning or end, and should not contain "sql" in the output.
    """
]

# Streamlit App
st.set_page_config(page_title="I can Retrieve Any SQL Query")
st.header("Gemini App To Retrieve the SQL Data")

question = st.text_input('Input:', key="input")

submit = st.button("Ask your question")

# If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print(response)

    # Fix: Clean up the response to remove markdown formatting
    query = response.text.strip("```sql").strip("```").strip()  

    data = read_sql_query(query, "student.db") 

    st.subheader("The Response is:")
    for row in data:
        print(row)
        st.header(row)
