# 연산자  산술, 비교, 논리
# 산술 : +, -, *, /(실수나누기), //(정수나누기), **(지수승), %(나머지)
# 비교 : >, >=, <. <=, ==, !=
# 논리 : and, or, not

# a, b = 5, 2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a**b)
# print(a%b)
# print("-"*50)
# a+=1;
# print(a)

# a, b = 5, 2
# print(a>b)
# print(a>=b)
# print(a<b)
# print(a<=b)
# print(a==b)
# print(a!=b)

# a="10"
# b="20"
# print(a+b)
# print(int(a)+int(b))


# a=10
# b=-5
# c=0
# d="hello"
# e=32.7
# f=0.0
# print(a,bool(a))
# print(b,bool(b))
# print(c,bool(c))
# print(d,bool(d))
# print(e,bool(e))
# print(f,bool(f))
# 0이 아닌 값이 있는 상태는 모두 True.


# print(int(True))
# print(int(False))
#1, 0


# name = input("이름을 입력하시오==>")
# print(name)


# 연습) 사용자한테 어떤 숫자 하나를 입력받아 +1을 하여 출력하기
# n = int(input("숫자를 입력하세요 ==>"))
# print(n+1)

# 연습) 사용자한테 나이를 입력받아 20이상인지 판별하여 True, False를 출력하기
# age = int(input('나이를 입력하세요: '))
# re = age >= 20
# print(re)
# age = int(input('나이를 입력하세요: '))
# re = age >= 20
# print(re)


# 연습) 두 사람의 나이를 입력받아 모두 20살 이상이면 True, 그렇지 않으면 False 출력하기
age1=int(input("첫번째 사람 나이를 입력하세요 ==>"))
age2=int(input("두번째 사람 나이를 입력하세요 ==>"))
re = age1 >= 20 and age2 >= 20
print(re)