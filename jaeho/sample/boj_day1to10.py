# #---------------Day1 (230731)---------------
# 2557
# print("Hello World!")


# 1000
# input_str = input().split()
# a = int(input_str[0])
# b = int(input_str[1])
# print(a + b)


# 1001
# input_str = input().split()
# a = int(input_str[0])
# b = int(input_str[1])
# print(a - b)


# 10998
# input_str = input().split()
# a = int(input_str[0])
# b = int(input_str[1])
# print(a * b)


# 1008
# input_str = input().split()
# a = int(input_str[0])
# b = int(input_str[1])
# print(a / b)


# # ---------------Day2 (230801)---------------
# # 10869
# a, b = input().split()
# a = int(a)
# b = int(b)
# print(a + b)
# print(a - b)
# print(a * b)
# print(a // b)
# print(a % b)


# # 10926
# print(input() + "??!")


# # 18108
# print(int(input()) - 543)


# # 10430
# a, b, c = map(int, input().split())
# print((a + b) % c)
# print(((a % c) + (b % c)) % c)
# print((a * b) % c)
# print(((a % c) * (b % c)) % c)
# # map으로 쪼개놔도 알아서 들어가는 군.


# # 2588
# a = int(input())
# b = input()
# for i in b[::-1]:
#     print(a * int(i))
# print(a * int(b))


# # ---------------Day3 (230802)---------------
# # 11382
# print(sum(map(int, input().split())))


# # 10171
# print(
#     """\    /\\
#  )  ( ')
# (  /  )
#  \(__)|"""
# )
# # '\'는 이스케이프 문자에 포함되는 기호라서 문자열에 단독으로 들어가는 경우 '\\' 이렇게 두 번 써야 인식된다.
# # 문제의 조건이 모양을 출력하는 것 외에도 간격이나 엔터키를 허용하지 않음.


# # 10172
# print(
#     '''|\\_/|
# |q p|   /}
# ( 0 )"""\\
# |"^"`    |
# ||_/=\\\\__|'''
# )


# # 1330
# a, b = map(int, input().split())
# print("==" if a == b else ">" if a > b else "<")


# # 9498
# score = int(input())  # 시험 점수가 정수로 주어지므로 int로 변환해도 무방.
# print(
#     "A"
#     if 90 <= score <= 100
#     else "B"
#     if 80 <= score < 90
#     else "C"
#     if 70 <= score < 80
#     else "D"
#     if 60 <= score < 70
#     else "F"
# )
# # 왜 자꾸 이런 식으로 포맷하는 겨..


# # ---------------Day4 (230803)---------------
# # 2753
# year = int(input())
# print(1 if (year % 4 == 0) & ((year % 100 != 0) | (year % 400 == 0)) else 0)


# # 14861
# quadrant = 1
# if int(input()) > 0:
#     pass
# else:
#     quadrant = 2

# if int(input()) > 0:  # 정수 x, y가 주어지므로 int
#     pass
# else:
#     quadrant = 5 - quadrant

# print(quadrant)
# # if문을 중첩하지 않고 만들어보고 싶어서 5에서 빼는 방식으로 만들었음.
# # 실제로 이런 식으로 해도 될지는 모르겠음.


# # 2884
# hour, minute = map(int, input().split())
# minute = hour * 60 + minute
# if minute >= 45:
#     minute -= 45
# else:
#     minute = 24 * 60 - (45 - minute)

# hour = minute // 60
# minute = minute % 60
# print(hour, minute)


# # 2525
# h, m = map(int, input().split())
# cooking_time = int(input())
# m = h * 60 + m + cooking_time
# h = (m // 60) % 24
# m = m % 60
# print(h, m)


# # 2480
# dice = list(map(int, input().split()))
# eq = 0

# dice.sort(reverse=True)
# if dice[0] == dice[1]:
#     eq += 1
# if dice[1] == dice[2]:
#     eq += 1

# if eq == 2:
#     print(10000 + dice[0] * 1000)
# elif eq == 1:
#     print(1000 + dice[1] * 100)
# else:
#     print(dice[0] * 100)


# # ---------------Day5 (230804)---------------
# # 2739
# n = int(input())
# for i in range(1, 10):
#     print(n, "*", i, "=", n * i)


# # 10950
# repeat = int(input())
# for i in range(repeat):
#     print(sum(map(int, input().split())))


# # 8393
# result = 0
# for i in range(int(input())):
#     result += i + 1
# print(result)


# # 25304
# import math

# total_price = int(input())
# for i in range(int(input())):
#     total_price -= math.prod(map(int, input().split()))
# if total_price == 0:
#     print("Yes")
# else:
#     print("No")


# # 25314
# import math

# long_cnt = math.ceil(int(input()) / 4)
# print("long " * long_cnt + "int")


# # ---------------Day6 (230805)---------------
# # 15552
# import sys

# repeat = int(sys.stdin.readline())
# for i in range(repeat):
#     print(sum(map(int, sys.stdin.readline().split())))


# # 11021
# import sys

# repeat = int(sys.stdin.readline())
# for i in range(repeat):
#     print("Case #{}: {}".format(i + 1, sum(map(int, sys.stdin.readline().split()))))


# # 11022
# import sys

# repeat = int(sys.stdin.readline())
# for i in range(repeat):
#     num1, num2 = map(int, sys.stdin.readline().split())
#     print("Case #{}: {} + {} = {}".format(i + 1, num1, num2, num1 + num2))


# # 2438

# for i in range(1, int(input()) + 1):
#     print("*" * i)


# # 2439

# width = int(input())
# for i in range(1, width + 1):
#     print(("*" * i).rjust(width))


# # ---------------Day7 (230806)---------------
# # 10952

# import sys

# while True:
#     num1, num2 = map(int, sys.stdin.readline().split())
#     if num1 == num2 == 0:
#         break
#     print(num1 + num2)


# # 10951
# import sys

# while True:
#     try:
#         num1, num2 = map(int, sys.stdin.readline().split())
#         if num1 == num2 == 0:
#             break
#         print(num1 + num2)
#     except:
#         break


# # 10807
# int(input())
# input_list = list(map(int, input().split()))
# print(input_list.count((int(input()))))


# # 10871

# N, X = map(int, input().split())
# seq = list(map(int, input().split()))
# for i in range(N):
#     if seq[i] < X:
#         print(seq[i], end=" ")


# # 10818

# input()
# seq = list(map(int, input().split()))
# print(min(seq), max(seq))


# # ---------------Day8 (230807)---------------
# # 2562
# import sys

# seq = []
# while True:
#     try:
#         seq.append(int(sys.stdin.readline()))
#     except:
#         break
# print(max(seq))
# print(seq.index(max(seq)) + 1)


# # 10810
# import sys

# N, M = map(int, input().split())
# basket = [0 for a in range(N)]
# for a in range(M):
#     i, j, k = map(int, sys.stdin.readline().split())
#     for b in range(i - 1, j):
#         basket[b] = k
# for a in basket:
#     print(a, end=" ")


# # 10813
# import sys

# N, M = map(int, input().split())
# basket = [i for i in range(1, N + 1)]

# for a in range(M):
#     i, j = map(int, sys.stdin.readline().split())
#     i -= 1
#     j -= 1
#     # temp = basket[i] # # '임시의'라는 뜻의 temporary의 준말.
#     # basket[j] = basket[i]
#     # basket[i] = temp
#     basket[i], basket[j] = basket[j], basket[i]  # 그런데 파이썬에선 이런 것도 가능하다고 한다.

# print(" ".join(map(str, basket)))

# # for문이나 배열의 순서 불러오기에서 자꾸 순서를 틀려먹는다.
# # 확실하게 머릿속으로 구현하고 들어가는 걸 연습해야 하나?


# # 5597
# import sys

# stud_list = [i for i in range(1, 31)]
# while True:
#     try:
#         input_num = int(sys.stdin.readline())
#         # 형 변환을 입력과 함께 바로 하는 것과,
#         # 일단 str로 저장하고 나중에 변환하는 것에 따라
#         # 오류 발생 여부가 달라지는데, 이유를 모르겠다.
#     except:
#         break
#     del stud_list[stud_list.index(input_num)]
# print("\n".join(map(str, stud_list)))


# # 3052
# import sys

# remain = []
# while True:
#     try:
#         remain.append(int(sys.stdin.readline()) % 42)
#     except:
#         break
# print(len(set(remain)))


# # ---------------Day9 (230808)---------------
# # 10811
# import sys

# n, m = map(int, input().split())
# basket = [a for a in range(1, n + 1)]

# for a in range(m):
#     temp = []
#     i, j = map(int, sys.stdin.readline().split())
#     i -= 1
#     j -= 1
#     for a in range(j - i + 1):
#         temp.append(basket[i + a])
#     for a in range(j - i + 1):
#         basket[i + a] = temp[-1 - a]
# print(" ".join(map(str, basket)))


# # 1546
# n = int(input())
# score = list(map(int, input().split()))
# total_score = 0
# for i in score:
#     total_score += (i / max(score)) * 100
# print(total_score / n)


# # 27866
# while True:
#     try:
#         s = input()
#         i = int(input())
#         print(s[i - 1])
#     except:
#         break


# # 2743
# print(len(input()))
# # 아니 뭐 어떨 때는 while 쓰라고 하고 어떨 때는 쓰지
# # 말라 하고 아주 이랬다저랬다 지맘대로네


# # 9086
# import sys

# for i in range(int(input())):
#     string = sys.stdin.readline().rstrip("\n")
#     print(string[0] + string[-1])


# # ---------------Day10 (230809)---------------
# # 11654
# print(ord(input()))


# # 11720
# n = int(input())
# list_num = input()
# total = 0
# for i in list_num:
#     total += int(i)
# print(total)


# # 10809
# s = input()
# alpha = [chr(i) for i in range(97, 123)]
# alpha_loc = []
# for i in alpha:
#     alpha_loc.append(s.find(i))
# print(" ".join(map(str, alpha_loc)))
# # join() 메소드 사용 시에는 데이터타입 상관없이 붙여주는 줄
# # 알았는데 아니고, str로 바꿔주어야 함.


# # 2675
# import sys

# t = int(input())
# for i in range(t):
#     r, s = sys.stdin.readline().split()
#     for i in s:
#         print(i * int(r), end="")
#     print()


# # 1152
# print(len(list(input().split())))
