def make_fortune():
    import csv
    import sqlite3
    import random
    import itertools
    import platform
    if platform.system() == "Windows":
        encord = "ANSI"
    elif platform.system() == "macOS":
        encord = "UTF-8"

    def sort_number(number):  # 1位には１位データ、2～8位には２位データ、41位以下には１１位データ、48位には48位データ、ほかは数/4データを適用
        if number == 1:
            return 1
        elif number <= 8:
            return 2
        elif number == 48:
            return 12
        elif number >= 41:
            return 11
        else:
            return -(-number // 4)

    sign_list = ["牡羊座", "牡牛座", "双子座", "蟹座", "獅子座", "乙女座", "天秤座", "蠍座", "射手座", "山羊座", "水瓶座", "魚座"]
    bloom_type = ["A型", "B型", "O型", "AB型"]
    sb_list = list(itertools.product(sign_list, bloom_type))#全通り取得
    random.shuffle(sb_list)
    conn = sqlite3.connect("uranai_DB.db")
    fortune_list = []
    for i in range(1, 48 + 1):
        sql = f"""
        SELECT comment
        FROM comment01
        WHERE number ={sort_number(i)};
        """
        results = conn.execute(sql).fetchall()
        sql2 = f"""
        SELECT comment
        FROM comment02
        WHERE number ={sort_number(i)};
        """
        results2 = conn.execute(sql2).fetchall()
        sql3 = "SELECT color,item FROM color_item;"
        results3 = conn.execute(sql3).fetchall()

        fortune_list.append([i, random.choice(results)[0], random.choice(results2)[0], random.choice(results3)[0],
                             random.choice(results3)[1], sb_list[i - 1][0], sb_list[i - 1][1]])
    conn.commit()
    conn.close()

    with open("fortune.csv", mode="w", encoding=encord, newline="") as f:
        w = csv.writer(f, delimiter=",")
        for i in range(len(fortune_list)):
            w.writerow(fortune_list[i])


if __name__ == '__main__':
    make_fortune()
