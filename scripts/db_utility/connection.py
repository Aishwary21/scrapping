from sqlalchemy import create_engine
import mysql.connector
from mysql.connector import Error

def conne(df):
    try:
        conn = mysql.connector.connect(user='root', 
                                       password="aishwary2001??", 
                                       host='localhost',
                                       port=3306,
                                       database='data_scrapper',
                                       )
        if conn:
            print("Connected to MySQL Server version")
            engine=create_engine('mysql://root:aishwary2001??@localhost/data_scrapper')
            df.to_sql(con=engine, name='scrapped_data', if_exists='append',index=False)
            conn.commit()
            print("Data Inserted")
    except Error as e:
        print(e)
    # finally:
    #     if conn:
    #         cursor.close()
            