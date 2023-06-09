#익명의 함수 lambda 함수 

def plus_one(x):
    return x+1

print(plus_one(1))

# lambda 함수를 호출하려면 변수에 넣어줘야 한다. 
plus_two = lambda x: x+2
print(plus_two(1))

# 이 함수는 내장함수의 인자로 사용할 떄 좋다. 
a = [1,2,3]
print(list(map(plus_one, a)))

print(list(map(lambda x: x+1, a))) # 이런식으로 한줄로 표현이 가능하다. 
