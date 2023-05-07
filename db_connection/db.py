

PG_HOST="43.137.10.2:5432"
PG_USER="postgres"
PG_PASSWORD="cZ6eMqv&AZ4P^uB2"
DB_NAME="postgres"




import os
import pandas as pd
import time
import datetime
from sqlalchemy import create_engine

engine = create_engine('postgresql://{}:{}@{}/{}'.format(PG_USER, PG_PASSWORD, PG_HOST, DB_NAME))

import sqlalchemy
from sqlalchemy import text


# read all excel and csv files from BASE_DIR and write to postgres
def write_to_db(dir, file_name = None):
    
    if file_name is None:
        
        for file in os.listdir(dir):
            if file.endswith('.xlsx') or file.endswith('.csv'):
                print('read {} to postgres'.format(file))
            
                # read excel file
                if file.endswith('.xlsx'):
                    df = pd.read_excel(os.path.join(dir, file))
                
                if file.endswith('.csv'):
                    df = pd.read_csv(os.path.join(dir, file))
                        
                write_to_postgres(df, file_name.split('.')[0], 'mfg', engine)


    elif file_name is not None:
        
        # read excel file
        if file_name.endswith('.xlsx'):
            df = pd.read_excel(os.path.join(dir, file_name))
        
        if file_name.endswith('.csv'):
            df = pd.read_csv(os.path.join(dir, file_name))
        

        write_to_postgres(df, file_name.split('.')[0], 'mfg', engine)


def write_to_db_df(df, table_name):
    
    write_to_postgres(df, table_name, 'mfg', engine)
        
    print('write {} to postgres'.format(table_name))
    
    
def test_db():
# create a table in pg with name test using sqlalchemy
    with engine.connect() as conn:
        
        sql = """DROP TABLE IF EXISTS mfg.test;"""
        conn.execute(text(sql))
        
        
        # create a new schema with name mfg in pg
        sql = """CREATE SCHEMA IF NOT EXISTS mfg;"""
        conn.execute(text(sql))
        
        
        sql = """CREATE TABLE mfg.test (ID SERIAL PRIMARY KEY, value VARCHAR(255));"""
        conn.execute(text(sql))
        
        conn.commit()
        
    # read data from postgres

    with engine.connect() as conn:

        df = pd.read_sql_table('test', con = conn, schema='mfg')
        
    # define a function to refresh data to postgres

def write_to_postgres(df, table_name, schema_name, engine):
    
    # log time 
    start_time = time.time()
    
    with engine.connect() as conn:
        
        df.to_sql(table_name, con=conn, schema=schema_name, if_exists='replace', index=False)
        conn.commit()
        
    # time elapsed in seconds
    time_elapsed_seconds = str(time.time() - start_time)
    
    print('write table {}  total rows: {} to postgres. Time elapsed {} secs'.format(table_name.split('.')[0], \
        df.shape[0], time_elapsed_seconds))
    
    return
        
        
if __name__ == "__main__":
    
    test_db()
    
    # test write to db
    df = pd.DataFrame({'value': ['a', 'b', 'c']})
    write_to_db_df(df, table_name='test')
    