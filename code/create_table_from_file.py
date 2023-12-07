import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("/Users/nurululum/Documents/DATA ENGINEER/PROJECT/PROJECT 3/source/users_w_postal_code.csv", sep = ",")

engine = create_engine("postgresql://postgres:digitalskola@127.0.0.1:5432/postgres")

df.to_sql("users_w_postal_code", engine)