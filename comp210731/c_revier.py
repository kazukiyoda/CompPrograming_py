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

# C回答例
# まずソートする
A.sort()
B.sort()
# 以下の内容を実装する
'''
実装内容としては
1. abs(Ai-Bj)の値が今までに調べた差分のいずれよりも小さければ暫定的な答えを変更する
2. その後AiとBjを比較する
3. Ai > BjならばBjをB_(j+1)に変えて次の操作
4. Ai <= Bjならばj < j'であるj'についてabsを調べる必要はない
A_(i+1)についてもj' < jであるj'についてabs(A(i+1)-Bj')の値を調べる必要はないため
A(i+1)とBjは次の操作を行う
5. i > Nまたはj > Mとなったならば操作を終了する
'''

'''
answer = 0
for i in range(N):
    for j in range(M):
        tmp = abs(A[i] - B[j])
        if j == 0:
            answer = tmp # 初期値の設定
        if A[i] > B[j]:
            break
        else:
'''

# きついっす