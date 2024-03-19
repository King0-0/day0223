# 파이썬에서의 자료구조
# list      tuple       set     dictionary
# [ ]       ( )         { }      { }

# JSON 형태의 데이터  (key, value)로 구성

# 파이썬에서는 다중대입이 가능
# a,b = 5,7
# print(a)    # 5
# print(b)    # 7

# data = 5,7    # paking 튜플임(데이터 안의 값은 2개로 묶여있음)
# print(data,type(data))
# a,b = data    # unpacking  데이터 묶은거 다시 풀기
# print(a)    # 5
# print(b)    # 7

a = {"홍길동",20,"서울시 마포구 서교동"}
b = {
    "name" : "홍길동",
    "age" : 20,
    "addr" : "서울시 마포구 서교동"
}
print(b.items())
print(b.keys())
print(b.values())


# row에 key, value를 패킹해서 한번에 가져옴
# for row in b.items():   # dic에 있는 items(항목을 하나씩 불러옴)
#     key,value = row     # unpacking
#     print(key,value)




# print(a,type(a))
# print(b,type(b))
#
# print(b['name'])
# print(b['age'])
# print(b['addr'])
