import mysql.connector

mydb = mysql.connector.connect(
            host="peagainc-database.cggf88dd0xkh.ap-southeast-1.rds.amazonaws.com",
            port="3306",
            user="admin",
            passwd="V7o9is6U9CbIl0EmD5W7",
            database="ollincafe",
            auth_plugin="mysql_native_password"
        )
cursor = mydb.cursor(buffered=True)