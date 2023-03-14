import os
 
DB_NAME = 'postgres'
DB_USERNAME = 'postgres'
DB_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DB_HOST = '127.0.0.1'
DB_PORT = '5432'


QUERY_PRICES_SQL = '''SELECT p.day, p.price 
                            FROM prices p 
                                LEFT JOIN ports p1 ON p.orig_code = p1.code
                                LEFT JOIN ports p2 ON p.dest_code = p2.code
                            WHERE %s IN (p.orig_code, p1.parent_slug) AND %s IN (p.dest_code, p2.parent_slug)
                                AND day BETWEEN %s AND %s 
                            ORDER BY p.day;'''