# # # # # # # # # # # # # # # 24267

# # # # # # # # # # # # # # # MenOfPassion(A[], n) {
# # # # # # # # # # # # # # #     sum <- 0;
# # # # # # # # # # # # # # #     for i <- 1 to n - 2
# # # # # # # # # # # # # # #     # \sum_{i=1}^{n-2} ?
# # # # # # # # # # # # # # #         for j <- i + 1 to n - 1
# # # # # # # # # # # # # # #         # n은 정해진 값이며, j는 i+1 ~ n-1이므로 n-j를 대입하면 n-i-1~n-n+1 = n-i-1~1 이때 이중for문이므로
# # # # # # # # # # # # # # #         # ? = \sum_{k=1}^{n-i-1} k
# # # # # # # # # # # # # # #             for k <- j + 1 to n
# # # # # # # # # # # # # # #             # 할당되는 값이 j+1 ~ n이므로 총 실행횟수는 n - j+1 + 1 = n-j
# # # # # # # # # # # # # # #                 sum <- sum + A[i] × A[j] × A[k];
# # # # # # # # # # # # # # #                 # 얘는 의미가 없음 내용과 상관없이 한 번 실행하기 때문.
# # # # # # # # # # # # # # #     return sum;
# # # # # # # # # # # # # # # }

# # # # # # # # # # # # # # # 1 2 3 4 5 6 ... n-4 n-3 n-2

# # # # # # # # # # # # # # # 1+1 2+1 3+1 ... n-4+1 n-3+1 n-2+1 -> 2 ~ n-1 ----> n-2 n-3 n-4 ~ 3 2 1

# # # # # # # # # # # # # # # 1+1+1 2+1+1 ... n-3+1+1 n-2+1+1 -> j+1 ~ n -> n - j

# # # # # # # # # # # # # # # n - 1 ~ 2

# # # # # # # # # # # # # # # 왜 아다리가 안맞을까.....................?

# # # # # # # # # # # # # # # 일단 공식은 n(n-1)(n-2)/2로 나온다.

# # # # # # # # # # # # # # n = int(input())
# # # # # # # # # # # # # # print(int((n * (n - 1) * (n - 2)) / 6))
# # # # # # # # # # # # # # print(3)

# # # # # # # # # # # # # #2798
# # # # # # # # # # # # # n, m = map(int, input().split())
# # # # # # # # # # # # # num_list = list(map(int, input().split()))
# # # # # # # # # # # # # num_1, num_2, num_3 = 0, 0, 0
# # # # # # # # # # # # # temp = 0
# # # # # # # # # # # # # result = 0
# # # # # # # # # # # # # for i in range(len(num_list)):
# # # # # # # # # # # # #     num_1 = num_list[i]
# # # # # # # # # # # # #     for j in range(len(num_list)):
# # # # # # # # # # # # #         if i != j:
# # # # # # # # # # # # #             num_2 = num_list[j]
# # # # # # # # # # # # #         else:
# # # # # # # # # # # # #             continue
# # # # # # # # # # # # #         for k in range(len(num_list)):
# # # # # # # # # # # # #             if (i != k) & (j != k):
# # # # # # # # # # # # #                 num_3 = num_list[k]
# # # # # # # # # # # # #             else:
# # # # # # # # # # # # #                 continue
# # # # # # # # # # # # #             temp = sum([num_1, num_2, num_3])
# # # # # # # # # # # # #             if (temp <= m) & (temp > result):
# # # # # # # # # # # # #                 result = temp
# # # # # # # # # # # # #             temp = 0
# # # # # # # # # # # # # print(result)

# # # # # # # # # # # # # 2231
# # # # # # # # # # # # n = int(input())
# # # # # # # # # # # # i = 0
# # # # # # # # # # # # disassemble = 0
# # # # # # # # # # # # while True:
# # # # # # # # # # # #     i += 1
# # # # # # # # # # # #     disassemble = 0
# # # # # # # # # # # #     if i > n:
# # # # # # # # # # # #         print(0)
# # # # # # # # # # # #         break
# # # # # # # # # # # #     for j in str(i):
# # # # # # # # # # # #         disassemble += int(j)
# # # # # # # # # # # #     if i + disassemble == n:
# # # # # # # # # # # #         print(i)
# # # # # # # # # # # #         break


# # # # # # # # # # # # 19532
# # # # # # # # # # # # a, b, c, d, e, f = map(int, input().split())
# # # # # # # # # # # # for x in range(-999, 1000):
# # # # # # # # # # # #     if x == ((c / b - f / e) / (a / b - d / e)):
# # # # # # # # # # # #         print(x, int((((-a) / b) * x) + (c / b)))
# # # # # # # # # # # #         break

# # # # # # # # # # # # 생각해보니까 방정식 다 풀어놓고 for문을 왜 돌려???
# # # # # # # # # # # # 코딩은 되는데 수학이 안된다. 이상하다...

# # # # # # # # # # # a, b, c, d, e, f = map(int, input().split())

# # # # # # # # # # # x = (c * e - f * b) / (a * e - d * b)
# # # # # # # # # # # y = (d * c - a * f) / (d * b - a * e)
# # # # # # # # # # # print(int(x), int(y))

# # # # # # # # # # # # 입력값으로 0이 들어갈 수 있으므로 식을 바꾸어야 함.


# # # # # # # # # # # 1018
# # # # # # # # # # import sys

# # # # # # # # # # a = [1, 0, 1, 0, 1, 0, 1, 0]
# # # # # # # # # # b = [0, 1, 0, 1, 0, 1, 0, 1]
# # # # # # # # # # chess_board_1 = 0
# # # # # # # # # # chess_board_2 = 0
# # # # # # # # # # recolor_1 = 0
# # # # # # # # # # recolor_2 = 0
# # # # # # # # # # recolor_numcase = []

# # # # # # # # # # m, n = map(int, input().split())
# # # # # # # # # # board = []
# # # # # # # # # # for i in range(m):
# # # # # # # # # #     board.append(list(sys.stdin.readline().rstrip()))
# # # # # # # # # #     board[i] = [0 if x == "B" else 1 for x in board[i]]
# # # # # # # # # # # for i in range(m):
# # # # # # # # # # # print(board[i])

# # # # # # # # # # for i in range(m - 8 + 1):
# # # # # # # # # #     for j in range(n - 8 + 1):
# # # # # # # # # #         chess_board_1 = [a.copy() if i % 2 == 0 else b.copy() for i in range(8)]
# # # # # # # # # #         chess_board_2 = [b.copy() if i % 2 == 0 else a.copy() for i in range(8)]

# # # # # # # # # #         # print("체스보드 1 - {} : {}".format(i, j))
# # # # # # # # # #         # for k in range(8):
# # # # # # # # # #         #     print(chess_board_1[k])
# # # # # # # # # #         # print("체스보드 2 - {} : {}".format(i, j))
# # # # # # # # # #         # for k in range(8):
# # # # # # # # # #         #     print(chess_board_1[k])

# # # # # # # # # #         for k in range(8):
# # # # # # # # # #             for l in range(8):
# # # # # # # # # #                 chess_board_1[k][l] += board[i + k][j + l]
# # # # # # # # # #                 chess_board_2[k][l] += board[i + k][j + l]
# # # # # # # # # #                 # 이걸 그냥 돌려버리면 점점 값이 추가되는 걸 볼 수 있는데 이유는 리스트의 주소만 복사해왔기 때문인 것 같다.
# # # # # # # # # #                 # 맞았다. chess_board를 만들 때 copy()메소드로 참조가 아니라 새로 만들어서 가져오는 것으로 했더니 제대로 동작함.
# # # # # # # # # #                 # 기존 코드의 문제는 chess_board는 새로 만들지만 그 안에 들어가는 1차원 리스트 a, b를 새로 만들어 가져오지 않고 주소만 참조해왔기 때문에
# # # # # # # # # #                 # 지속적으로 a, b에 값이 추가됐던 것이다.

# # # # # # # # # #                 chess_board_1[k][l] %= 2
# # # # # # # # # #                 chess_board_2[k][l] %= 2

# # # # # # # # # #         # print("체스보드 1 수정본 - {} : {}".format(i, j))
# # # # # # # # # #         # for k in range(8):
# # # # # # # # # #         #     print(chess_board_1[k])
# # # # # # # # # #         # print("체스보드 2 수정본 - {} : {}".format(i, j))
# # # # # # # # # #         # for k in range(8):
# # # # # # # # # #         #     print(chess_board_2[k])

# # # # # # # # # #         recolor_1 = sum(sum(chess_board_1[i]) for i in range(8))
# # # # # # # # # #         recolor_2 = sum(sum(chess_board_2[i]) for i in range(8))
# # # # # # # # # #         recolor_numcase.append(min(recolor_1, recolor_2))
# # # # # # # # # # # print(recolor_numcase)
# # # # # # # # # # print(min(recolor_numcase))

# # # # # # # # # # # # 2751
# # # # # # # # # # # import sys

# # # # # # # # # # # num = []
# # # # # # # # # # # for i in range(int(input())):
# # # # # # # # # # #     num.append(int(sys.stdin.readline()))

# # # # # # # # # # # num = sorted(num)
# # # # # # # # # # # for i in num:
# # # # # # # # # # #     print(i)


# # # # # # # # # # 1436
# # # # # # # # # n = int(input())
# # # # # # # # # nth_title = 0
# # # # # # # # # title = 0

# # # # # # # # # while True:
# # # # # # # # #     title += 1
# # # # # # # # #     if str(title).find("666") != -1:
# # # # # # # # #         nth_title += 1
# # # # # # # # #         # print(title, end=", ")
# # # # # # # # #     if nth_title == n:
# # # # # # # # #         # print()
# # # # # # # # #         print(title)
# # # # # # # # #         break


# # # # # # # # # 1157
# # # # # # # # string = list(input().upper())
# # # # # # # # alpha = set(string)
# # # # # # # # cnt = {}

# # # # # # # # for i in alpha:
# # # # # # # #     cnt[i] = string.count(i)

# # # # # # # # temp = [i for i, j in cnt.items() if j == max(cnt.values())ㅡㅐ]
# # # # # # # # if len(temp) > 1:
# # # # # # # #     print("?")
# # # # # # # # else:
# # # # # # # #     print(temp[0])


# # # # # # # # 2839

# # # # # # # n = int(input())
# # # # # # # fi_kg = 0
# # # # # # # th_kg = 0
# # # # # # # while True:
# # # # # # #     if th_kg * 3 > n:
# # # # # # #         print(-1)
# # # # # # #         break

# # # # # # #     if (n - th_kg * 3) % 5 == 0:
# # # # # # #         fi_kg = (n - th_kg * 3) // 5
# # # # # # #         print(th_kg + fi_kg)
# # # # # # #         break

# # # # # # #     th_kg += 1

# # # # # # 1012

# # # # # # import sys

# # # # # # for i in range(int(input())):  # 첫 줄에 입력된 횟수만큼 돌림.
# # # # # #     m, n, k = map(int, input().split())
# # # # # #     cabbage = []
# # # # # #     num_cluster = 0

# # # # # #     for j in range(k):  # k개의 양배추의 위치를 가져옴.
# # # # # #         cabbage.append(list(map(int, sys.stdin.readline().split())))
# # # # # #     # print(cabbage)

# # # # # #     while len(cabbage) > 0:
# # # # # #         cluster = []
# # # # # #         cluster.append(cabbage.pop(0))
# # # # # #         while True:
# # # # # #             wow = 0
# # # # # #             for j in cluster:
# # # # # #                 for l in ["top", "bottom", "left", "right"]:
# # # # # #                     tblr = (
# # # # # #                         [j[0] - 1, j[1]]
# # # # # #                         if l == "top"
# # # # # #                         else [j[0] + 1, j[1]]
# # # # # #                         if l == "bottom"
# # # # # #                         else [j[0], j[1] - 1]
# # # # # #                         if l == "left"
# # # # # #                         else [j[0], j[1] + 1]
# # # # # #                     )
# # # # # #                     if tblr in cabbage:
# # # # # #                         cluster.append(cabbage.pop(cabbage.index(tblr)))
# # # # # #                         wow = 1
# # # # # #             if wow == 0:
# # # # # #                 num_cluster += 1
# # # # # #                 break
# # # # # #     print(num_cluster)


# # # # # # 1019

# # # # # n = int(input())
# # # # # long_string = ""
# # # # # cnt_num = []

# # # # # for i in range(1, n + 1):
# # # # #     long_string += str(i)

# # # # # for i in range(10):
# # # # #     print(long_string.count(str(i)), end=" ")
# # # # # print()

# # # # # # 위의 코드는 메모리 사용량이 너무 큰가 보다.
# # # # # # 느려서 시간초과가 떠서 공식을 찾아보기로 했다.
# # # # # l
# # # # # # n = int(input());
# # # # # temp = 0

# # # # # for i in range(1, len(str(n))):
# # # # #     temp += (n // (10**i)) * (10 ** (i - 1))

# # # # # num_cnt = [temp for _ in range(10)]
# # # # # print(num_cnt)

# # # # # for i in range(len(str(n)) - 1, -1, -1):
# # # # #     temp = (n // (10**i)) % 10
# # # # #     if temp != 0:
# # # # #         for j in range(1, temp):
# # # # #             num_cnt[j] += 10**i
# # # # #     num_cnt[temp] += n % (10**i) + 1

# # # # # print(" ".join(map(str, num_cnt)))


# # # # import sys

# # # # def factorial(num):
# # # #     for i in range(num - 1, 0, -1):
# # # #         num *= i
# # # #     return num

# # # # for i in range(int(input())):
# # # #     n, m = map(int, sys.stdin.readline().split())
# # # #     if n == m:
# # # #         print(1)
# # # #         continue
# # # #     m_n = factorial(m - n)
# # # #     n = factorial(n)
# # # #     m = factorial(m)
# # # #     print(m // (m_n * n))


# # # # 2566
# # # max_num = 0
# # # col = 0
# # # row = 0
# # # for i in range(9):
# # #     line = list(map(int, input().split()))
# # #     if max(line) > max_num:
# # #         max_num = max(line)
# # #         col = i + 1
# # #         row = line.index(max_num) + 1
# # # print(max_num)
# # # print(col, row)


# # # 1120
# # a, b = input().split()
# # difference = -1
# # if len(a) == len(b):
# #     temp = 0
# #     for i in range(len(a)):
# #         if a[i] != b[i]:
# #             temp += 1
# #     difference = temp
# # else:
# #     for i in range(len(b) - len(a) + 1):
# #         temp = 0
# #         for j in range(len(a)):
# #             if a[j] != b[i + j]:
# #                 temp += 1
# #         if (difference > temp) | (difference == -1):
# #             difference = temp
# # print(difference)


# # 1003

# import sys

# # def fibonacci(n):
# #     if n == 0:
# #         return 0
# #     elif n == 1:
# #         return 1
# #     else:
# #         return fibonacci(n - 1) + fibonacci(n - 2)


# def fibonacci(n):
#     result = (1 / (5 ** (1 / 2))) * (
#         ((1 + (5 ** (1 / 2))) / 2) ** n - ((1 - (5 ** (1 / 2))) / 2) ** n
#     )
#     return int(result)


# for i in range(int(input())):
#     n = int(sys.stdin.readline())
#     if n == 0:
#         print(1, 0)
#     else:
#         print(fibonacci(n - 1), fibonacci(n))


# 1244
import sys


def student(num):
    if num[0] == 1:
        for i in range(num[1], len(switch) + 1):
            if i % num[1] == 0:
                switch[i - 1] = 0 if switch[i - 1] else 1
    elif num[0] == 2:
        radial = 0
        num[1] -= 1
        while True:
            if (num[1] - radial < 0) | (num[1] + radial >= len(switch)):
                break
            else:
                if switch[num[1] - radial] == switch[num[1] + radial]:
                    radial += 1
                else:
                    break
        radial -= 1
        for i in range(num[1] - radial, num[1] + radial + 1):
            switch[i] = 0 if switch[i] else 1


input()
num = []
switch = list(map(int, input().split()))
for i in range(int(input())):
    num = list(map(int, sys.stdin.readline().split()))
    student(num)


times = 0
while len(switch) != 0:
    print(switch.pop(0), end=" ")
    times += 1
    if times == 20:
        print()
        times = 0
