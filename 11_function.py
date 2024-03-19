# 함수 : 어떤 문제해결을 위한 서로 관련있는 명령어들의 집합
'''
def 함수명():
    명령어들
    return [값1, 값2, 값3,...]    반환하는 타입 : 튜플

파이썬의 함수는 여러개의 값으로 반환이 가능
이것을 packing해서 tuple로 받거나
unpacking하여 따로 받을 수 있음.
'''

# 두 개의 수를 매개변수로 전달받아 더하기하여 결과를 돌려주는 함수
# def add(a,b):
#     r = a + b
#     return r
#
# r = add(5,2)
# print(r)
# print(add(5, 2))
# print(add(8, 15))


# 연습) 두 개의 수를 매개변수로 전달받아
# 더하기, 빼기, 곱하기, 나누기한 결과를 반환하는 함수를 만들어 보기
def calc(a,b):
    add = a+b
    sub = a-b
    multi = a*b
    div = a//b
    return  add,sub,multi,div

# 함수표출결과를 tuple로 패킹해서 가져오기 (여러개를 구해서 튜플형태로 반환함)
data = calc(5,2)
print(data,type(data))

# 함수표출결과를 unpackking해서 받아오기
add,sub,multi,div = calc(5,2)
print(add,sub,multi,div,type(data))