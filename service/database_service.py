import config
import pymysql

try:
    db = pymysql.connect(config.DATABASE_URL, config.USERNAME, config.PASSWORD, config.DATABASE)
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    print('[MySQL Version: ' + cursor.fetchone()[0] + ']\n')
except (pymysql.err.OperationalError, pymysql.err.InternalError) as err:
    print(err)
    exit(2)

# MYSQL GRANT REMOTE ACCESS
# GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'yourpassword' WITH GRANT OPTION; for all databases
# GRANT ALL PRIVILEGES ON DB.* TO 'root'@'%' IDENTIFIED BY 'yourpassword' WITH GRANT OPTION; for database DB

# SQL QUERIES
# cursor.execute(query)

# GET RESULTS
# cursor.fetchone()
# cursor.fetchall()
# cursor.fetchmany(size)

# INSERT
# sql = "INSERT INTO 'tablename' ('field1', 'field2') VALUES (%s, %s)"
# cursor.execute(sql, ('value1', 'value2')
