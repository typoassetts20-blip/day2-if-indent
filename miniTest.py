# 課題テーマ：リストと条件分岐の組み合わせ
# 好きな物を5つ、リストに入れる
# 変数にすきな文字を入力
# 入力された名前がリストにあれば「○○はリストにあります！」、なければ「○○はリストにありません」と表示する

favlist = ["apple","orange", "fish","tea","coffee"]

item = "apple" # 入力を受け付ける場合は input()

if  item in favlist :
    print("contain")
else :
    print ("not exist")

item2 = "tomato"

if  item2 in favlist :
    print("contain")
else :
    print ("not exist")