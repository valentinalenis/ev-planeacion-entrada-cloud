import mysql.connector  as mysql
import config

cnx = mysql.MySQLConnection(
    host = config.host,
    port = config.port,
    user = config.user,
    password = config.password,
    database = config.database
)




