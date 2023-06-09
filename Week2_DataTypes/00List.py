a = []
b = [1, 2, 3]
c = ['a', 'b', 'c', 'Life']
d = [1, 2, 'a', 'b']
e = [1, 2, ['a', 'b', 'c']]
f = list([1, 2, 3])

# 인덱싱과 슬라이싱

## 인덱싱 
e[0]
e[-1]
e[2]

e[-1][2]

## 슬라이싱
e[0:2]
e[-1][1:]

# 리스트의 수정과 삭제
e[1] = 3    # 수정

del e[0]    # 삭제

del e[-1][0:-1]     # 삭제 (슬라이싱과 2차원 리스트)

list = [1,2, 'A', 'a', ["Life", "Is"], '  Too', 'Short  '] # 여러가지 자료형을 담은 리스트 선언
list.insert(3, 'B')     # list[3] 위치에 'B' 삽입  
# list = [1, 2, 'A', 'B', 'a', ['Life', 'Is'], '  Too', 'Short  ']

# 리스트 관련 함수