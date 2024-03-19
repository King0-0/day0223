# 파이썬에서의 자료구조
# list      tuple       set     dictionary
# [ ]       ( )         { }      { }

# 튜플 : 리스트의 상수버전
a = [1,3,5,7]   # 리스트
b = (1,3,5,7)   # 튜플
b = list(b)     # 튜플 >> 리스트로 바꾸기
print(type(b))
b.append(9)     # 튜플을 리스트로 바꿔서 요소를 추가해
b[0] = 100      # 이하동문
b = tuple(b)    # 리스트였던것을 다시 튜플로 되돌리기
print(type(b))
print(b)


# print(a,type(a))
# print(b,type(b))
#b.append(10)    # 튜플에는 추가못해
#print(b)

# print(b[0])     # 1
# # b[0] = 100    # 대입은 안돼
# # 튜플에서 수정하고 싶다면, 리스트로 만들어서 수정 후 다시 튜플로 돌려라
# for i in b:
#     print(i,end=" ")    #데이터에 접근하는 방법은 동일함