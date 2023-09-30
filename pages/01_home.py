import streamlit as st
import psycopg2
import pandas as pd



"""
Certainly, let's break down this code snippet:

1. **Importing Libraries:**
    - `import streamlit as st`: Import Streamlit library for creating web apps.
    - `import psycopg2`: Import psycopg2 library for interacting with a PostgreSQL database.
    - `import pandas as pd`: Import the Pandas library for data manipulation.

2. **Variable Definition:**
    - `my_var = "Dirk"`: A variable `my_var` is initialized with the value "Dirk".

3. **Streamlit Frontend:**
    - `st.title(f"Kashi's famous artist is {my_var}")`: Sets the title of the Streamlit web app, and includes the value of `my_var`.
    - `st.write("We create a web front end in Streamlit and are connecting to a PostgresDB within a Docker container.")`: Writes a text string explaining what the web app does.
    - `st.write("hhttps://docs.streamlit.io/library/api-reference")`: Writes a hyperlink to Streamlit's API documentation (note: the 'h' before 'https' seems like a typo).

This is a very basic Streamlit application that displays some text and a title on a web page. It imports the psycopg2 library, which suggests that it might connect to a PostgreSQL database in the future, but there is no code doing that yet.

The code is not yet connecting to any database within a Docker container, even though one of the `st.write()` statements implies that. To actually connect to a PostgreSQL database, you'd use psycopg2's connection methods, but those aren't implemented in this code snippet.
"""

my_var = "Dirk"

st.title(f"Kashi's famous artist is {my_var}")
st.write("We create a web front end in Streamlit and are connecting to a PostgresDB within a Docker container.")
st.write("https://docs.streamlit.io/library/api-reference")

"""






"""
# Database connection parameters
params = {
    'host': 'localhost',
    'port': 5432,
    'dbname': 'pagila',
    'user': 'ui',
    'password': '1234567890'
}

# Connect to the PostgreSQL database
conn = psycopg2.connect(**params)

# Execute a query to fetch all table names
cur = conn.cursor()
cur.execute("""
SELECT table_name FROM information_schema.tables
WHERE table_schema = 'public';
""")
tables = cur.fetchall()

# Close cursor
cur.close()

# Create a dropdown for users to select a table
table = st.selectbox('Select a table:', [x[0] for x in tables])

# Show table content
if table:
    # Query the table and load it into a DataFrame
    query = f"SELECT * FROM {table};"
    df = pd.read_sql(query, conn)

    # Display the DataFrame in Streamlit
    st.write(f"Displaying data from `{table}`")
    st.dataframe(df)

# Close the database connection
conn.close()


# Simulate a database using Python dictionaries
user_db = {}
activity_db = {
    'Soccer': 'Berlin Central Park, 10am-12pm, Age 7-12',
    'Swimming': 'Berlin Pool, 2pm-4pm, Age 5-10'
}

# Function to handle user registration
def register_user(username, password):
    if username in user_db:
        st.warning("Username already exists.")
        return
    user_db[username] = password
    st.success(f"User {username} successfully registered.")

# Function to authenticate user
def authenticate(username, password):
    if username in user_db and user_db[username] == password:
        return True
    return False

# Function to list activities
def list_activities():
    st.write("## Available Sports Activities for Children in Berlin")
    for activity, details in activity_db.items():
        st.write(f"**{activity}**: {details}")

# Main App
st.title("Sports Activities for Children in Berlin")

# menu = ["Home", "Login", "Register"]
# choice = st.sidebar.selectbox("Menu", menu)

choice = Home

if choice == "Home":
    st.write("## Welcome to our platform")
    st.write("Please login to see and book activities")

elif choice == "Login":
    st.subheader("Login to Your Account")
    username = st.text_input("User Name")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        if authenticate(username, password):
            st.success("Logged In")
            list_activities()
        else:
            st.warning("Invalid Credentials")

elif choice == "Register":
    st.subheader(":orange[Please register to use the Kids Sports App]")

    full_name = st.text_input("Full name")
    address = st.text_input("Address")
    phone = st.text_input("Phone")
    email = st.text_input("Email")
    
    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type='password')

    if st.button("Register"):
        register_user(new_user, new_password)
