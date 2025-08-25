# Day2: if文とインデント事故
# 1.基本のif文
x = 10
if x > 5:
    print("xは5より大きい")

# if-else文
if x % 2 == 0:
    print("xは偶数")
else:
    print("xは奇数")

# if-elif-else文
score = 92
if  score >= 90:
    print("評価A")
elif score >= 70: # else if ではない
    print("評価B")
else:
    print("評価C")

# 2.インデント評価の例
# if  score >= 90: 
# print("評価A") #IndentationError: expected an indented block after 'if' statement on line 22
# VScode使用時もインデントなしだとエラー表示される。 

# C#のように書くとエラー
# if (score == 90) {  VSCodeで　：が必要です表示
#    print("評価A")
# }

# インデント量の確認
if score >= 90:
 print("インデント1")

if score >= 90:
  print("インデント2")

if score >= 90:
    print("インデント3")

if score >= 90:
     print("インデント5")
#          print("不揃いインデント5_2") #実行エラー unexpected indent