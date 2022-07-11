import mysql.connector

def fetch_data(n):
    conn = mysql.connector.connect(user='root', 
                                       password="aishwary2001??", 
                                       host='localhost',
                                       port=3306,
                                       database='data_scrapper',
                                       )
    cursor = conn.cursor()
    cursor.execute("select count(*) from scrapped_data")
    
    result=tuple()
    for _ in range(1,n):     
        result.append(cursor.fetchone())
    
    
   
    
    return result