import psycopg2
from utils.constants import QUERY_PRICES_SQL

class Database:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def connect(self):
        try:
            conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            return conn
        except Exception as e:
            print("Unable to connect to the database: %s" % e)
            return None

    def fetch_rates(self, date_from, date_to, origin, destination):
            conn = self.connect()
            if conn:
                cursor = conn.cursor()
                try:
                    cursor.execute(QUERY_PRICES_SQL,(origin, destination, date_from, date_to))
                    rows = cursor.fetchall()
                    if rows:
                        return rows
                    else:
                        print("Unable to retrieve prices from the database.")
                        return None
                finally:
                    conn.close()