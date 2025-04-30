**Used TIDB for connecting and executing the database

import pandas as pd
from sqlalchemy import create_engine

# Database connection details
host = "gateway01.us-west-2.prod.aws.tidbcloud.com"
user = "4TMDeET5hb2Bj8r.root"
password = "5rkxQxG1OohjStR2"
port = 4000
database = "test"

# Create the SQLAlchemy engine for the connection
engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}")

# Load the CSV file
csv_file_path = r"C:\Users\HP\thriller_2024_movies_og2.csv"
df = pd.read_csv(csv_file_path)
print(f"✅ CSV loaded: {df.shape[0]} rows × {df.shape[1]} cols")

# Upload the DataFrame to the database
df.to_sql('thriller_2024', con=engine, if_exists='replace', index=False)
print(f"📤 Data uploaded to `thriller_2024`")

# After uploading the data, check if the table exists in the database
with engine.connect() as conn:
    result = conn.execute("SHOW TABLES")
    tables = result.fetchall()
    print(f"✅ Tables in the database: {tables}")

    if ('thriller_2024',) in tables:
        print("✅ Table `thriller_2024` exists.")
    else:
        print("❌ Table `thriller_2024` does not exist.")
