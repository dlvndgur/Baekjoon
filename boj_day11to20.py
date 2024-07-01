# # ---------------Day11 (230810)---------------
# 2908
# a, b = map(int, "".join(reversed(input())).split())
# print(max(a, b))


# 5622
# dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
# time = 0
# call = input()
# for i in call:
#     for j in range(len(dial)):
#         if i in dial[j]:
#             time += j + 3
# print(time)

# # 단순한 구조가 생각이 안나서 결국 찾아보고 했음.
# # 그래도 별로라서 원본코드도 첨부.

# # dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# # a = input()
# # ret = 0
# # for j in range(len(a)):
# #     for i in dial:
# #         if a[j] in i:
# #             ret += dial.index(i)+3
# # print(ret)


# # 11718
# import sys

# while True:
#     string = sys.stdin.readline().rstrip("\n")
#     if string != "":
#         print(string)
#     else:
#         break


# # 25083
# print(
#     """         ,r'"7
# r`-_   ,'  ,/
#  \. ". L_r'
#    `~\/
#       |
#       |"""
# )


# # 3003
# # import numpy as np

# # black = np.array([1, 1, 2, 2, 2, 8])
# # white = np.array(list(map(int, input().split())))
# # print(" ".join(map(str, black - white)))
# # # numpy의 array 클래스도 리스트처럼 맵으로 데이터 변환 가능

# # ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 넘파이는 표준라이브러리가 아니라 사용할 수 없다고 한다...

# black = [1, 1, 2, 2, 2, 8]
# white = list(map(int, input().split()))
# for i in range(len(black)):
#     print(black[i] - white[i], end=" ")


# # ---------------Day12 (230811)---------------
# # 2444
# num = int(input())
# for i in range(1, num):
#     print(" " * (num - i) + "*" * (2 * i - 1))
# for i in range(num, 0, -1):
#     print(" " * (num - i) + "*" * (2 * i - 1))


# # 10988
# pelin = input()
# is_pelindrom = 1
# for i in range(len(pelin)):
#     if pelin[i] != pelin[len(pelin) - i - 1]:
#         is_pelindrom = 0
#         break
# print(is_pelindrom)


# # 1157
# string = input().upper()
# alpha = list(set(string))
# alpha_cnt = {}
# for i in alpha:
#     alpha_cnt[i] = string.count(i)

# cnt = [k for k, v in alpha_cnt.items() if max(alpha_cnt.values()) == v]
# if len(cnt) == 1:
#     print(cnt[0])
# else:
#     print("?")


# # 2941
# croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
# word = input()
# alpha_cnt = 0
# loc = -1
# for i in croatia:
#     alpha_cnt += word.count(i)
#     word = " ".join(word.split(i))
# alpha_cnt += len("".join(word.split()))
# print(alpha_cnt)

# # 훨씬 간단한 코드가 있어서 가져옴.
# x = input()
# cro_al = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
# for i in cro_al:
#     x = x.replace(i, "a")
# print(len(x))


# 1316
# group_word = 0
# for _ in range(n):
#     word = input()
#     error = 0
#     for index in range(len(word) - 1):  # 인덱스 범위 생성 : 0부터 단어개수 -1까지
#         if word[index] != word[index + 1]:  # 연달은 두 문자가 다른 때,
#             new_word = word[index + 1 :]  # 현재글자 이후 문자열을 새로운 단어로 생성
#             if new_word.count(word[index]) > 0:  # 남은 문자열에서 현재글자가 있있다면
#                 error += 1  # error에 1씩 증가.
#     if error == 0:
#         group_word += 1  # error가 0이면 그룹단어
# print(group_word)


# # ---------------Day13 (230812)---------------
# # 25206
# import sys

# # grade point : 과목 점수
# grade_point = {
#     "A+": 4.5,
#     "A0": 4.0,
#     "B+": 3.5,
#     "B0": 3.0,
#     "C+": 2.5,
#     "C0": 2.0,
#     "D+": 1.5,
#     "D0": 1.0,
#     "F": 0.0,
# }
# credit_sum = 0
# # major grade point average : 과목 평균 점수
# mgpa = 0
# for i in range(20):
#     _, cr, gp = sys.stdin.readline().split()
#     if gp == "P":
#         continue
#     mgpa += float(cr) * grade_point[gp]
#     credit_sum += float(cr)
# print("%0.6f" % (mgpa / credit_sum))


# # 2738
# import sys

# n, m = map(int, input().split())
# procession = []
# for i in range(n):
#     sub = list(map(int, sys.stdin.readline().split()))
#     # 리스트로 선언한 sub에 map으로 넣으면 map 객체가 들어가버림.
#     procession.append(sub)
# for i in range(n):
#     sub = list(map(int, sys.stdin.readline().split()))
#     for j in range(m):
#         procession[i][j] += sub[j]
#         print(procession[i][j], end=" ")
#     print()


# # 2566
# import sys

# grid = []
# row = 0
# col = 0
# max_num = 0
# for i in range(9):
#     sub = list(map(int, sys.stdin.readline().split()))
#     if max(sub) > max_num:
#         max_num = max(sub)
#         row = i
#     grid.append(sub)
# print(max_num)
# print(row + 1, grid[row].index(max_num) + 1)


# # 10798
# import sys

# youngseok = []
# max_len = 0
# for i in range(5):
#     row = sys.stdin.readline().rstrip()
#     max_len = max(max_len, len(row))
#     youngseok.append(row)
# # print(youngseok)
# for i in range(5):
#     youngseok[i] = list(youngseok[i].ljust(max_len, " "))
# # print(youngseok)
# for i in range(max_len):
#     for j in range(5):
#         if youngseok[j][i] != " ":
#             print(youngseok[j][i], end="")

# # 더 짧고 간단하게 하는 방법이 있을까...?

# arr = [[""] * 15 for _ in range(5)]
# # 최대 15개 글자이므로 위와 같이 제한할 수 있다.
# # 문제에 주어진 조건을 잘 활용하자.

# # 이렇게 간단할 수가...
# i = 0
# for _ in range(5):
#     j = 0
#     for c in input():  # 문자열은 그냥 써도 된다.
#         arr[i][j] = c
#         j += 1
#         # j를 이렇게 처리한 이유는 input()의 길이에 따라 변하도록 하기 위해서.
#     i += 1

# for j in range(15):
#     for i in range(5):
#         print(arr[i][j], end="")


# # 2563
# import sys

# canvas = [[0 for _ in range(100)] for _ in range(100)]
# # arr = [[0] * 100 for _ in range(100)]
# # 이차원 배열 선언은 이렇게 하면 된다.
# # print(canvas)
# area = 0
# for _ in range(int(input())):
#     x, y = map(int, sys.stdin.readline().split())
#     # 1st n -> 왼쪽 벽과 왼쪽 변 사이 -> x
#     # 2nd n -> 아래쪽 벽과 아래쪽 변 사이 -> y
#     for i in range(10):
#         for j in range(10):
#             canvas[100 - 1 - (y + i)][x + j] = 1

# for i in canvas:
#     for j in i:
#         area += j
# print(area)


# # ---------------Day14 (230813)---------------
# # 2745
# b, n = input().split()
# n = int(n)
# decimal = 0
# digit = 0
# for i in b[::-1]:
#     try:
#         decimal += int(i) * (n**digit)
#     except:
#         decimal += (ord(i) - 55) * (n**digit)
#     digit += 1
# print(decimal)

# # 아스키코드 변환
# # 숫자->문자 chr : character '문자'
# # 문자->숫자 ord : ordinal '순서'->아스키코드 순서 얘기하는 듯.


# # 11005
# n, b = map(int, input().split())
# result = ""
# remainder = 0
# while True:
#     remainder = n % b
#     n = n // b
#     result += str(remainder) if remainder < 10 else chr(remainder + 55)
#     if n == 0:
#         break
# print(result[::-1])


# # 2720
# import sys


# def divide(to_div, div_with):
#     quotient = to_div // div_with
#     remainder = to_div % div_with
#     return quotient, remainder


# for _ in range(int(input())):
#     penny = int(sys.stdin.readline())
#     quarter, penny = divide(penny, 25)
#     dime, penny = divide(penny, 10)
#     nickel, penny = divide(penny, 5)
#     print(quarter, dime, nickel, penny)


# # 2903
# initial = 2
# for i in range(int(input())):
#     initial = 2 * initial - 1
# print(initial**2)


# # 2292
# n = int(input())
# room = 0
# while True:
#     if n <= 0:
#         break
#     room += 1
#     if room == 1:
#         n -= 1
#         continue
#     n -= 6 * (room - 1)
# print(room)


# # ---------------Day15 (230814)---------------
# # 1193
# x = int(input())
# i = 1
# j = 1
# while True:
#     if x - i <= 0:
#         break
#     x -= i
#     i += 1
#     j += 1
# if j % 2 == 1:
#     print("{}/{}".format(j - x + 1, x))
# else:
#     print("{}/{}".format(x, j - x + 1))


# # 2869
# import sys

# a, b, v = map(int, sys.stdin.readline().split())
# day = (
#     ((v - a) // (a - b)) + 2
#     if ((v - a) / (a - b)) > ((v - a) // (a - b))
#     else ((v - a) // (a - b)) + 1
# )
# print(day)


# # 5086
# import sys

# a, b = map(int, sys.stdin.readline().split())

# while not (a == b == 0):
#     if b % a == 0:
#         print("factor")
#     elif a % b == 0:
#         print("multiple")
#     else:
#         print("neither")
#     a, b = map(int, sys.stdin.readline().split())


# # 2501
# n, k = map(int, input().split())
# divisors = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         divisors.append(i)
# try:
#     print(divisors[k - 1])
# except:
#     print(0)


# # 9506
# import sys

# n = int(sys.stdin.readline())
# while n != -1:
#     divisors = []
#     for i in range(1, n + 1):
#         if (n % i == 0) & (i != n):
#             divisors.append(i)
#     if sum(divisors) == n:
#         print(f"{n} = {' + '.join(map(str, divisors))}")
#     else:
#         print(f"{n} is NOT perfect.")
#     n = int(sys.stdin.readline())


# # ---------------Day16 (230815)---------------
# # 1978
# n = input()
# num_list = list(map(int, input().split()))
# prime_num = []
# for i in num_list:
#     is_prime = True
#     if i < 2:
#         continue
#     if i == 2:
#         prime_num.append(2)
#         continue
#     for j in range(2, i):
#         if i % j == 0:
#             is_prime = False
#     if is_prime == True:
#         prime_num.append(i)
# print(len(prime_num))


# # 2581
# m = int(input())
# n = int(input())
# prime_num = []
# for i in range(m, n + 1):
#     if i == 2:
#         prime_num.append(2)
#         continue
#     if i < 2:
#         continue
#     is_prime = True
#     for j in range(2, i):
#         if i % j == 0:
#             is_prime = False
#     if is_prime == True:
#         prime_num.append(i)
# if len(prime_num) > 0:
#     print(sum(prime_num))
#     print(min(prime_num))
# else:
#     print(-1)

# # 주워온 거
# # import sys
# # import math

# # m = int(sys.stdin.readline().rstrip())
# # n = int(sys.stdin.readline().rstrip())  # m부터 n까지 중에 소수 골라내기.

# # array = [True for i in range(n + 1)]  # 배열에 n+1개의 True를 담아줌.

# # for i in range(2, int(math.sqrt(n)) + 1):  # math.sqrt()함수는 제곱근을 반환하는 함수.
# #     if array[i] == True:  # i=2부터 i의 값에 1씩 더해가며 array[i]가 소수인 경우
# #         j = 2  # j를 초기화하고
# #     while i * j <= n:
# #         array[i * j] = False  # 소수의 곱에 해당하는 모든 수에 소수가 아님을 표시.
# #         j += 1  # i는 고정, j는 1씩 커짐. 즉, i의 모든 배수에 False

# # prime_numbers = [
# #     i for i in range(m, n + 1) if array[i] and i != 1
# # ]  # 오.. array를 이런 식으로 선언할 수 있는지 몰랐다.
# # # True, False로 표시한 배열에서 True이고, i가 1이 아닌 경우에만 소수 배열에 추가.

# # if prime_numbers:  # 이건 뭐지. 배열에 값이 없으면 False로 값이 나타나나 보다?
# #     # 배열이 빈 배열인지 확인하는 방법이 두가지인데, len(array)하고 not array(그냥 array도 되겠지 당연히)가 있다고 한다.
# #     print(sum(prime_numbers))
# #     print(min(prime_numbers))
# # else:
# #     print(-1)


# # 11653
# prime_factor = []
# i = 2
# n = int(input())
# if n == 1:
#     exit
# while True:
#     if n % i == 0:
#         n /= i
#         prime_factor.append(i)
#         i = 2
#     else:
#         i += 1
#     if n == 1:
#         break
# for i in prime_factor:
#     print(i)


# # 27323
# print(int(input()) * int(input()))


# # 1085
# import sys
# x, y, w, h = map(int, sys.stdin.readline().split())
# print(min(w-x, x, h-y, y))


# # ---------------Day17 (230816)---------------
# # 3009
# import sys

# x = {}
# y = {}
# for _ in range(3):
#     xx, yy = map(int, sys.stdin.readline().split())
#     try:
#         x[xx] += 1
#     except:
#         x[xx] = 1
#     try:
#         y[yy] += 1
#     except:
#         y[yy] = 1
# print(min(x, key=x.get), min(y, key=y.get))


# # 15894
# print(4 * int(input()))


# # 9063
# import sys

# x = []
# y = []
# for _ in range(int(input())):
#     xx, yy = map(int, sys.stdin.readline().split())
#     x.append(xx)
#     y.append(yy)
# print((max(x) - min(x)) * (max(y) - min(y)))


# # 10101
# import sys

# a = int(sys.stdin.readline())
# b = int(sys.stdin.readline())
# c = int(sys.stdin.readline())
# if sum([a, b, c]) != 180:
#     print("Error")
# elif a == b == c == 60:
#     print("Equilateral")
# elif (a == b) | (b == c) | (a == c):
#     print("Isosceles")
# else:
#     print("Scalene")


# # 5073
# import sys

# while True:
#     a, b, c = map(int, sys.stdin.readline().split())
#     if sum([a, b, c]) == 0:
#         break
#     if max(a, b, c) >= (sum([a, b, c]) - max(a, b, c)):
#         print("Invalid")
#     elif a == b == c:
#         print("Equilateral")
#     elif (a == b) | (b == c) | (a == c):
#         print("Isosceles")
#     else:
#         print("Scalene")


# # ---------------Day18 (230904)---------------
# # 14215
# stick = list(map(int, input().split()))
# max_round = 0
# for i in range(3):
#     for j in range(stick[i]):
#         stick_2 = stick.copy()
#         stick_2[i] -= j
#         if (max(stick_2) * 2 < sum(stick_2)) & (max_round < sum(stick_2)):
#             max_round = sum(stick_2)
# print(max_round)


print('와')
print('wow')