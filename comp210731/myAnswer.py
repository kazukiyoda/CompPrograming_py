# UTF-8
# A問題
input_line = input().split(" ")
A = int(input_line[0])
B = int(input_line[1])

if A > 0:
    if B == 0:
        print("Gold") # 純金
    else:
        print("Alloy") # 合金
else:
    print("Silver") # 純銀

# B問題
# 4桁の数字が入力されるので分割して配列に格納
input_number = input()
x = [int(i) for i in list(input_number)] # listにするときに全てint型に直しておく

# Weak条件1
if x[0] == x[1]:
    if x[1] == x[2]:
        if x[2] == x[3]:
            print("Weak")
            exit()

# Weak条件2
# 1~3桁目に関して、右隣の桁がその桁の+1である場合
# ただし9の隣は0として考える
flag = 0
for i in range(3):
    x_now = x[i] + 1
    if x_now == 10:
        x_now = 0
    if x_now == x[i+1]:
        flag = 1
    if x_now != x[i+1]:
        flag = 0
        break

if flag == 0:
    print("Strong")
else:
    print("Weak")

# C問題
# 問題なのは実行時間がやばすぎること
input_line = input().split(" ")
N = int(input_line[0])
M = int(input_line[1])
inpt_A = input().split(" ")
A = [int(i) for i in inpt_A]
# print(A)
inpt_B = input().split(" ")
B = [int(i) for i in inpt_B]
# print(B)

# 個々の処理は工夫する必要がある
answer = 1000000000 - 1
for Ai in A:
    for Bj in B:
        tmp = abs(Ai - Bj)
        if answer > tmp:
            answer = tmp

print(answer)

# C回答例
