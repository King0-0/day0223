import re

db = '''
3412    Bob 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1234  Tiger 567
1548  Kerry 534
'''

print(db)
'''
?   1번 이하   colou?r ==> color, colour
*   0번 이상   ab?c    ==> ac, abc, abbc, abbbc
+   1번 이상   ab+c    ==> abc, abbc, abbbc    (not ac)
'''


# 숫자만 출력하기
# db로부터 패턴을 찾아라
# result = re.findall("[0-9]+",db)  #위 db목록에서 숫자만 배열로 출력됨
# print(result)   #list 타입
# print(type(result))


# 연습) 이름만 출력하기
# names = re.findall("[A-z]+",db)
# names = re.findall("[A-Z][a-z]+",db)
# print(names)


# 연습) 전화번호만 출력하기 (앞에 4자리)
# phones = re.findall("[0-9][0-9][0-9][0-9]",db)
# phones2 = re.findall("[0-9]{4}",db)
# phones3 = re.findall("\d{4}",db)
# phones4 = re.findall("^\d+",db,re.MULTILINE)
#re.MULTILINE : 찾고자 하는 데이터가 줄마다 있음.

# print(phones)
# print(phones2)
# print(phones3)
# print(phones4)


# 연습) 아이디만 추출하여 출력해보기
# ids = re.findall("\d+$",db,re.MULTILINE)
# print(ids)


# 연습) T로 시작하는 이름만 찾아서 출력하기
# startT = re.findall("T[a-z]+",db)
# print(startT)


# 연습) T로 시작하지 않는 이름만 출력하기
# notT = re.findall("[^T][a-z]+",db) #이러면 T만 없어지고 T로 시작하는 애도 없어짐...
notT = re.findall("[A-SU-Z][a-z]+",db)
print(notT)