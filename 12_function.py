# 연습) 두 개의 수를 매개변수로 전달받아
# 그 중에 큰 수를 찾아 반환하는 함수 만들고 호출하기

# **** 선생님 방법 ****
def max(a,b):
    if b>a: a=b
    return a

# 연습) 3개의 수를 매개변수로 전달받아 (위 함수 활용)
# 그 중 큰 수를 찾아 반환하는 함수를 만들고 호출하기
a = int(input("첫 번쨰 수를 입력하세요 ==> "))
b = int(input("두 번쨰 수를 입력하세요 ==> "))
c = int(input("세 번쨰 수를 입력하세요 ==> "))

def max3(a,b,c):
    return max(max(a,b),c)

print(max3(a,b,c))