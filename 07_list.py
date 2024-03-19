# 파이썬에서의 자료구조
# list      tuple       set     dictionary
# [ ]       ( )        { }     { }

a = [1,3,5,7]

#리스트에 데이터 추가하기
a.append(9)
print(a)

#리스트 맨 앞에 추가하기
a[0] = 100
print(a)


# # 연습) 리스트의 요소를 거꾸로 출력해봅시다.
# for i in range(len(a)-1,-1,-1):     #0은 포함이 안되니까 -1
#     print(a[i],end=" ")
# print()
# for i in reversed(a):   #a를 거꾸로 뒤집어줌 : 7,5,3,1
#     print(i, end=" ")


# print(a)
# print(type(a))
# # [1, 3, 5, 7]
#
# print(a[0]) #1
# print(a[1]) #3
#
# print(len(a))   #4  (배열 길이)


# for i in range(0,len(a)):
#     print(a[i],end=" ")     # 1 3 5 7
# print()
# for i in range(len(a)):
#     print(a[i],end=" ")     # 1 3 5 7
# print()
# for i in a:
#     print(i,end=" ")        # 1 3 5 7