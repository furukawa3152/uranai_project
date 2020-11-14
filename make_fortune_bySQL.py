import csv
import sqlite3
from pprint import pprint
import random

conn = sqlite3.connect("uranai_DB.db")
fortune_list=[]
for i in range(1,12+1):
    sql=f"""
    SELECT comment
    FROM comment01
    WHERE number ={i};
    """
    results = conn.execute(sql).fetchall()
    sql2=f"""
    SELECT comment
    FROM comment02
    WHERE number ={i};
    """
    results2=conn.execute(sql2).fetchall()
    sql3="SELECT color,item FROM color_item;"
    results3=conn.execute(sql3).fetchall()
    fortune_list.append([i,random.choice(results)[0],random.choice(results2)[0],random.choice(results3)[0],random.choice(results3)[1]])
conn.commit()
conn.close()
with open("fortune.csv", mode ="w", encoding="ANSI",newline="") as f:
    w=csv.writer(f, delimiter=",")
    for i in range(len(fortune_list)):
        w.writerow(fortune_list[i])

