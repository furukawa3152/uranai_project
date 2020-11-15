import csv
from pprint import pprint
import sqlite3

uranaicomment_list1=[]#占いコメント１作成
with open("uranaicomment1.csv", "r") as f:
    reader =csv.reader(f)
    for i in reader:
        uranaicomment_list1.append(i)

uranai_list1=[]
for i in range(len(uranaicomment_list1)):
    uranai_list1.append([int(uranaicomment_list1[i][0]),uranaicomment_list1[i][1]])

conn =sqlite3.connect("uranai_DB.db")
sql ="""
     CREATE TABLE comment01(
       number INTEGER,
       comment TEXT);
"""
conn.execute(sql)
for i in range(len(uranai_list1)):
    number = uranai_list1[i][0]
    comment = uranai_list1[i][1]
    sql ="INSERT INTO comment01(number,comment)VALUES(?,?)"
    conn.execute(sql, (number, comment))

conn.commit()
conn.close()
uranaicomment_list2=[]#占いコメント2作成
with open("uranaicomment2.csv", "r") as f:
    reader =csv.reader(f)
    for i in reader:
        uranaicomment_list2.append(i)

uranai_list2=[]
for i in range(len(uranaicomment_list2)):
    uranai_list2.append([int(uranaicomment_list2[i][0]),uranaicomment_list2[i][1]])

conn =sqlite3.connect("uranai_DB.db")
sql ="""
     CREATE TABLE comment02(
       number INTEGER,
       comment TEXT);
"""
conn.execute(sql)
for i in range(len(uranai_list2)):
    number = uranai_list2[i][0]
    comment = uranai_list2[i][1]
    sql ="INSERT INTO comment02(number,comment)VALUES(?,?)"
    conn.execute(sql, (number, comment))

conn.commit()
conn.close()

color_item=[]#カラー、アイテムDB作成
with open("coloritem.csv", "r") as f:
    reader =csv.reader(f)
    for i in reader:
        color_item.append(i)

conn =sqlite3.connect("uranai_DB.db")
sql ="""
     CREATE TABLE color_item(
       color TEXT,
       item TEXT);
"""
conn.execute(sql)
for i in range(len(color_item)):
    color = color_item[i][0]
    item = color_item[i][1]
    sql ="INSERT INTO color_item(color,item)VALUES(?,?)"
    conn.execute(sql, (color, item))

conn.commit()
conn.close()