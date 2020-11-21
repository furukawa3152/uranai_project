import csv
import datetime
import platform
import make_fortune_bySQL

if platform.system() == "Windows":
    encord = "ANSI"
elif platform.system() == "macOS":
    encord = "UTF-8"

dt_now = datetime.datetime.now()
today = f"{dt_now.year}年{dt_now.month}月{dt_now.day}日"
with open("last.fetch.csv", mode="r") as f:
    last_fetch = f.read()

if today != last_fetch:
    print(f"{today}の占い作成中")
    make_fortune_bySQL.make_fortune()
    print("見えました！！")
    with open("last.fetch.csv", mode="w", encoding=encord, newline="")as f:
        f.write(today)


def run_uranai(sign: int, blood: int):
    fortune_list = []
    sign_dict = {1: "牡羊座", 2: "牡牛座", 3: "双子座", 4: "蟹座", 5: "獅子座", 6: "乙女座", 7: "天秤座", 8: "蠍座", 9: "射手座", 10: "山羊座",
                 11: "水瓶座", 12: "魚座"}
    blood_dict = {1: "A型", 2: "B型", 3: "O型", 4: "AB型"}
    sign = sign_dict[sign]
    blood = blood_dict[blood]
    with open("fortune.csv", "r") as f:
        reader = csv.reader(f)
        for i in reader:
            fortune_list.append(i)

        for i in range(len(fortune_list)):
            if sign == fortune_list[i][5] and blood == fortune_list[i][6]:
                answer = fortune_list[i]
                return f"{answer[5]}で{answer[6]}のあなた、今日は48位中{answer[0]}位の日！\n{answer[1]}。{answer[2]}。\n" \
                       f"ラッキーアイテムは{answer[4]},ラッキーカラーは{answer[3]}だよ。"


if __name__ == '__main__':
    print("星座番号を入力してね\n1:牡羊座 2:牡牛座 3:双子座 4:蟹座 5:獅子座 6:乙女座 7:天秤座 8:蠍座 9:射手座 10:山羊座 11:水瓶座 12:魚座")
    sign = int(input())
    print("血液型を番号で入力してね\n1:A型　2:B型 3:O型 4:AB型")
    blood = int(input())
    print(run_uranai(sign, blood))
