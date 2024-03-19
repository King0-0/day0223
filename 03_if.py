'''
if문의 형식

if문의 조건식:
    명령어1
    명령어2
    ...
else:
    명령어3
    명령어4
    ..
'''


# 연습) 어떤 수를 입력받아 짝수인지 홀수인지 판별하여 출력하기
# n = int(input("숫자를 입력하시오 : "))
# if n%2==0:
#     print('짝수')
# else:
#     print('홀수')


# 연습) 사용자에게 3개의 숫자를 입력받아 그 중 가장 큰 수를 찾아 출력하기
# a = int(input("첫 번째 숫자를 입력하세요 ==> "))
# b = int(input("두 번째 숫자를 입력하세요 ==> "))
# c = int(input("세 번째 숫자를 입력하세요 ==> "))
# if a>b:
#     if a>c:
#         max=a
#     else:
#         max=c
# else:
#     if b>c:
#         max=b
#     else:
#         max=c
# print("가장 큰 수는 ==>",max)


'''
    물어봐야 할 것이 많다면 elif를 사용하기(JAVA의 else if와 같음)
    if 조건1:
        명령1
    elif 조건2:
        명령2
    elif 조건3:
        명령3
        ...
    else:
        ..
'''

# 연숩) 0~9 사이의 정수를 입력받아 한글 표기식을 출력하는 코드를 작성하기
# n = int(input("0~9 사이의 숫자를 하나 입력하세요 ==>"))
# if n == 0:
#     print("영")
# elif n ==1:
#     print("일")
# elif n == 2:
#     print("이")
#     ...

n = int(input("0~9 사이의 숫자를 하나 입력하세요 ==>"))
if n>=0 and n<=9:
    if n == 0 : kor = "영"
    elif n == 1 : kor = "일"
    elif n == 2 : kor = "이"
    elif n == 3 : kor = "삼"
    elif n == 4 : kor = "사"
    elif n == 5 : kor = "오"
    elif n == 6 : kor = "육"
    elif n == 7 : kor = "칠"
    elif n == 8 : kor = "팔"
    elif n == 9 : kor = "구"
    print(kor)
else:
    print("입력범위를 초과하였습니다.")