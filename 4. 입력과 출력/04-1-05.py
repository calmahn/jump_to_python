def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

    #매개변수 이름 앞에 *을 붙이면 입력값을 전부 모아 튜플로 만들어줌

result1 = add_many(1,2,3)
result2 = add_many(1,2,3,4,5,6,7,8,9,10)
print(result1);print(result2)