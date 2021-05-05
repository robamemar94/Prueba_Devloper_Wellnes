import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from app.api.models import Energy, db
import pandas as pd


# Create the database
db.drop_all()
db.create_all()

path = basedir = os.path.abspath(os.path.dirname(__file__))
csv_file_path = os.path.join(path,'Monitoring_report.csv')

# Read CSV with Pandas
with open(csv_file_path, 'r') as file:
    df = pd.read_csv(file)

engine = db.get_engine()
df.columns = Energy.__table__.columns.keys()
df=df[~df.date.duplicated()]
df.date = pd.to_datetime(df.date,format='%d %b %Y %H:%M:%S')

# Insert to DB
df.to_sql('energia',
          con=engine,
          index=False,
          if_exists='append')

db.session.commit()