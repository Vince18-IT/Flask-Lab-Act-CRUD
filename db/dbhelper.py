'''
    dbhelper
'''
from sqlite3 import connect, Row 

database: str = "db/school.db"

def createDB() -> None:
    conn: any = connect(database)
    cursor: any = conn.cursor()
    conn.row_factory = Row
    
    sql: str = "CREATE TABLE IF NOT EXISTS `students`(id integer primary key autoincrement, idno varchar(10) unique, lastname varchar(50), firstname varchar(50), course varchar(10), level varchar(5))"
    cursor.execute(sql)
    
    sql_users: str = "CREATE TABLE IF NOT EXISTS `users`(id integer primary key autoincrement, email varchar(100) unique, password varchar(100), name varchar(100))"
    cursor.execute(sql_users)
    
    cursor.close()
    conn.close()

def addstudent(**kwargs) -> bool:
    keys: list = list(kwargs.keys())
    vals: list = list(kwargs.values())
    fields: str = ",".join(keys)
    data: str = "','".join(vals)
    sql: str = f"INSERT INTO `students`({fields}) VALUES('{data}')"
    
    conn: any = connect(database)
    cursor: any = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    rc = cursor.rowcount
    cursor.close()
    conn.close()
    
    return True if rc > 0 else False

def adduser(**kwargs) -> bool:
    keys: list = list(kwargs.keys())
    vals: list = list(kwargs.values())
    fields: str = ",".join(keys)
    data: str = "','".join(vals)
    sql: str = f"INSERT INTO `users`({fields}) VALUES('{data}')"
    
    conn: any = connect(database)
    cursor: any = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    rc = cursor.rowcount
    cursor.close()
    conn.close()
    
    return True if rc > 0 else False

def getprocess(sql: str, vals: list) -> list:
    print(sql)
    conn: any = None
    cursor: any = None
    data: list = []
    try:
        conn = connect(database)
        conn.row_factory = Row
        cursor = conn.cursor()
        cursor.execute(sql, vals)
        data = cursor.fetchall()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return data

def getall(table: str) -> list:
    sql: str = f"SELECT * FROM `{table}`"
    return getprocess(sql, [])
    
def getrecord(table: str, **kwargs) -> list:
    keys: list = list(kwargs.keys())
    vals: list = list(kwargs.values())
    flds: list = []
    
    [flds.append("`"+key+"`=?") for key in keys]
    fld: str = " AND ".join(flds)
    sql: str = f"SELECT * FROM `{table}` WHERE {fld}"
    return getprocess(sql, vals)

def updatestudent(idno: str, **kwargs) -> bool:
    keys = list(kwargs.keys())
    vals = list(kwargs.values())
    set_clause = ", ".join([f"`{k}`=?" for k in keys])
    sql = f"UPDATE `students` SET {set_clause} WHERE `idno`=?"
    
    conn = connect(database)
    cursor = conn.cursor()
    cursor.execute(sql, vals + [idno])
    conn.commit()
    rc = cursor.rowcount
    cursor.close()
    conn.close()
    return rc > 0
   
def deleterecord(table: str, **kwargs) -> bool:
    keys: list = list(kwargs.keys())
    vals: list = list(kwargs.values())
    flds: list = []
    
    [flds.append("`"+key+"`=?") for key in keys]
    fld: str = " AND ".join(flds)
    sql: str = f"DELETE FROM `{table}` WHERE {fld}"
    
    conn: any = connect(database)
    cursor: any = conn.cursor()
    cursor.execute(sql, vals)
    conn.commit()
    rc = cursor.rowcount
    cursor.close()
    conn.close()
    
    return True if rc > 0 else False
    
def main() -> None:
    createDB()
    
    users_to_add = [
        {"email": "alpha@uc.com", "password": "hello123", "name": "alpha"},
        {"email": "bravo@uc.com", "password": "hello123", "name": "bravo"},
        {"email": "charlie@uc.com", "password": "hello123", "name": "charlie"}
    ]

    for user in users_to_add:
        try:
            adduser(**user)
            print(f"Successfully added user: {user['email']}")
        except Exception as e:
            print(f"Skipped user {user['email']} (might already exist)")

if __name__ == "__main__":
    main()