import re
import requests

#  아래 url에 있는 내용을 긁어서 출력
# <title> 안의 내용만 긁어오기
url = "https://devweather.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
text = requests.get(url).text
# print(text)

title = re.findall("<title>기상청 육상 중기예보</title>",text)
print()
# <title> 안의 내용만 가져오고 싶을 때 아무글자나 찍기 (. )
title2 = re.findall("<title>(.+)</title>",text)

# print(title)    # ['<title>기상청 육상 중기예보</title>']    리스트
# print(title2)
#
# for row in title:   # <title>기상청 육상 중기예보</title>    문자열
#     print(row)


# *****************************
# *****************************

# re.DOTALL ==> 찾고자 하는 시작, 마지막 패턴이 여러줄에 걸쳐서 있음
# 시작패턴 : <location wl_ver="3">  마지막패턴: </location>
# .+    ==> 탐욕적(한덩어리)
# .+?   ==> 비탐욕적(여러덩어리)

# 탐욕적(.+) : 찾고자 하는 패턴이 여러덩어리가 있을 때 한 덩어리로 가지고옴
# re.findAll("<location wl_ver="3">(.+)</location>)",text,re.DOTALL)
# 비탐욕적(.+?) : 찾고자 하는 패턴이 여러덩어리가 있을 때 한 덩어리로 가지고옴


# # 탐욕적 (1개)      (list)
# list = re.findall('<location wl_ver="3">(.+)</location>',text,re.DOTALL)
# print(len(list),type(list))

# 비탐욕적 (41개)    (list)
list2 = re.findall('<location wl_ver="3">(.+?)</location>',text,re.DOTALL)
print(len(list2))
print()
# *****************************
# *****************************

'''
<tmEf>2024-02-26 00:00</tmEf>
<wf>맑음</wf>
<tmn>-1</tmn>
<tmx>7</tmx>
'''

# 연습) 모든 도시명과 추출하여 출력 해보기.
# location안에 city가 있고 그 안에 data(날씨, 최저기온, 최고기온, 날짜)가 13개가 있음
# location을 찾아서 그 안에서 루프를 돌아
for row in list2:
    city = re.findall("<city>(.+)</city>", row) # city가 안많으니까 그냥 row하고 끝
    data = re.findall("<data>(.+?)</data>", row, re.DOTALL)
    for d in data :
        tmEf = re.findall('<tmEf>(.+?)</tmEf>',d)  # data만큼 루프를 돌아야됨
        wf = re.findall('<wf>(.+?)</wf>',d)
        tmn = re.findall('<tmn>(.+?)</tmn>',d)
        tmx = re.findall('<tmx>(.+?)</tmx>',d)
        # print(city, tmEf, wf, tmn, tmx)     # 값이 하나밖예 없어도 전체 리스트를 반환함(모든지역이뜸)
        print(city[0], tmEf[0], wf[0], tmn[0], tmx[0])

