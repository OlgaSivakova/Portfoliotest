import sqlite3 as sq

with sq.connect('userstests.db') as con:# connect with bd and close bd
    cur = con.cursor()
     #cur.execute("""CREATE TABLE IF NOT EXISTS tests (
    #    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #    name TEXT NOT NULL,
    #    sex TEXT,
    #    old INTEGER,
    #    data REAL
    #)
    # """) создать можно один раз
    #cur.execute("""CREATE TABLE IF NOT EXISTS tests (
    #    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #    pay INTEGER
    #    
    #)
    # """) 
    cur.execute("""CREATE TABLE IF NOT EXISTS additional_city (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT NOT NULL
        
    )
     """) 
    cur.execute("""CREATE TABLE IF NOT EXISTS additional_tel (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        tel INTEGER NOT NULL,
        tel_id INTEGER,
        FOREIGN KEY (tel_id)  REFERENCES additional_city (user_id)
        
    )
     """) 
    #cur.execute("UPDATE  userstests set data=13.08")
    #cur.execute("SELECT  name, old, data FROM userstests WHERE old>24")
    #cur.execute("select  name,  city, tel  from additional_city LEFT JOIN userstests on additional_city.user_id=userstests.user_id LEFT JOIN additional_tel ON additional_tel.tel_id=additional_city.user_id")
    
    #result = cur.fetchall() либо так и принтуем резулт ДЛЯ СЕЛЕКТА
    #for result in cur: #либо так и выводим кортеж в отдельной строке ДЛЯ СЕЛЕКТА
        #print(result)
    
    #result = cur.fetchall()
    #print(result)
    








