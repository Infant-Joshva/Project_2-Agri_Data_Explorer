import streamlit as st
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, inspect

# Load data from CSV
agri_df = pd.read_csv("data\\agri_data.csv")

# Connect to PostgreSQL
db_url = "postgresql://postgres:Admin@localhost:5432/Agri_db"
engine = create_engine(db_url)

# Write the DataFrame to SQL (replace if exists)
#agri_df.to_sql('agri_data', engine, index=False, if_exists='replace')

# Read back the data for testing
query = "SELECT * FROM agri_data"
df = pd.read_sql(query, engine)

# Display in Streamlit for verification (optional)
st.write("Data loaded from agri_data table:")
st.dataframe(df)

# inspector = inspect(engine)
# columns = inspector.get_columns('agri_data')
# for col in columns:
#     print(col['name'], col['type'])

