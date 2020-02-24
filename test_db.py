import psycopg2

is_exit = False

while not is_exit:
    try:
        conn = psycopg2.connect("user='postgres' host='db' password='123456' connect_timeout=1")
        conn.close()
        print('Connection to database is successful')
        is_exit = True
    except:
        print('Connection to database is unsuccessful')
        continue

exit(0)
