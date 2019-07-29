import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    load data into staging tables 
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    insert data into fact and dimension tables from staging tables
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()
        


def main():
    """
    connect database and load data into and insert from staging tables
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)
    

    conn.close()


if __name__ == "__main__":
    main()