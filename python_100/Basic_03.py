#문제 
# 아래 코드의 결과로 출력되는 값들에 대해서 설명하시오.
# id() 함수는 무엇을 출력하는가?
# 3개의 id 출력 값중 다른 값을 출력하는 것이 있다면 몇번이고 왜 그런지 그 이유를 설명하시오.
# [1]
# a = '붕어빵'
# print( a, ' --> ', id(a) )
# # [2]
# b=a
# print( b, ' --> ', id(b) )
# # [3]
# a = '잉어빵'
# print( a, ' --> ', id(a) )

#문제
# a, b 각각의 변수에 들어있는 값을 교환하는 코드를 작성하시오. 
# # a, b 변수에 들어있는 값은 100, 200 이다.
from re import A


a = 100 
b = 200
# temp 변수를 이용한 swap 
temp = a
a = b 
b = temp 

print('교환후a,b변수의값은 =', a, b)

a = 100 
b = 200
# temp 변수를 이용하지 않고 swap 
a, b = b, a
print('교환후a,b변수의값은 =', a, b)