print('hello world')

# 변수 & 기본연산
a = 3
b = a
a = a + 1

num1 = a*b
num2 = 99

# 자료형
name = 'bob'
num = 12

is_number = True

# 리스트형
a_list = []
a_list.append(1)
a_list.append([2, 3])

# a_list 값은 ? [1,[2,3]]
# a_list[0] 값은 ? 1
# a_list[1] 값은 ? [2,3]
# a_list[1][0] 값은 ? 2

# 딕셔너리 형
a_dict = {}
a_dict = {'name' : 'bob', 'age':21}
a_dict['height'] = 127

# a_dict 값은 ? {'name' : 'bob', 'age':21, 'height' : 178}
# a_dict['name'] 값은 ? 'bob'
# a_dict['age'] 값은 ? 21
# a_dict['height'] 값은 ? 178

# 딕셔너리와 리스트형의 조합
people = [{'name' : 'bob', 'age' : 21}, {'name' : 'carry', 'age' : 38}]

#people[0]['name'] 값은 ? 'bob'
#people[1]['name'] 값은 ? 'carry'

person = {'name' : 'john', 'age' : 7}
people.append(person)

# people의 값은? [{'name':'bob','age':20},{'name':'carry','age':38},{'name':'john','age':7}]
# people[2]['name']의 값은? 'john'

# 함수
f(x) = 2*x+3
y = f(2)
# y의값은 ? 7

# 자바스크립트에서는
#function f(x){
#    return 2*x+3
#}

# 파이선에서는
def f(x):
    return 2*x+3

# 함수의 응용

def sum_all(a,b,c):
    return a+b+c

def mul(a,b):
    return a*b

result = sum_all(1,2,3) + mul(10,10)

# 조건문

def oddeven(num):
    if num % 2 == 0:
        return True
    else:
        return False

def checkbob(name):
    if name == 'bob'
        return True
    else:
        return False

# 반복문
def allsum(mylist):    #allsum이라는 이름의 함수를 정의하고 mylist를 변수로 받는다.
    sub = 0            #sum이라는 변수에 0을 넣는다.
    for i in mylist:   #mylist의 원소들을 처음부터 돌면서, i에 넣어 아래 식을 수행한다.
        sum = sum + i  #sum에다 직전 sum에다 원소를 더한 값을 넣는다.
    return sum         #최종 sum을 반환한다.

sth_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(allsum(sth_list)) # 45

# 또는 자동으로 리스트를 생성해주는 파이썬 자체함수 range(숫자)를 사용하면,
sth_list_2 = range(10)  # [0,1,2,3,4,5,6,7,8,9] 와 같음
print(allsum(sth_list_2)) # 45

people = [{'name' : 'bob', 'age' : 20},
          {'name' : 'carry', 'age' : 38},
          {'name' : 'john', 'age' : 7}]

for person in people:
    print(person['name'], person['age'])

#반복문과 조건문을 응용한 함수
#이름을 받으면 age를 리턴해주는 함수
def get_age(myname):
    for person in people:
        if person['name'] == myname:
            return person['age']
    return '해당하는 이름이 없습니다.'

print(get_age('bob'))
print(get_age('katy'))