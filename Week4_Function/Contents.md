# 목차
> 1. 함수
> 2. 사용자 입출력
> 3. 파일 읽고 쓰기

- - -
## 1. 함수
### 함수의 구조
```
def {함수명}({매개변수}):
    {수행할 문장1}
    {수행할 문장2}
    ...
    return {반환값}
```

함수를 호출하게 되면 해당 함수로 이동하여 함수를 수행한다. (중간에 return이 있다면 반환값을 return하고 함수 종료).    
반환값, 매개변수 생략 가능   
함수 내의 변수는 함수 내에서만 사용한다.   

### - 디폴트 매개변수
매개변수는 기본값을 지정해줄 수 있다.   
기본값 지정시 함수를 호출 할때 인수값을 생략할 수 있다.   
변수에는 함수를 할당할 수 있으며, 매개변수에도 적용할 수 있다.   
   
### - 람다함수
람다함수는 익명함수로 함수를 간단히 사용할 수 있게 해준다.   
이름이 없기 때문에 아래와 같이 이름을 부여해 사용할 수 있으며 함수의 매개변수로 넘겨줄때도 사용한다.   
.   
.   
.   
- - -
## 2. 사용자 입출력
### - 입력
```
input({출력내용})   # 문자열로 반환
```

반환하는 문자열을 변수로 받아 사용할 수 있다.   
출력내용이 있으면 내용을 출력하고 입력을 *문자열*로 반환한다.   
입력으로 연산을 한다면 *숫자형*으로 캐스팅(형변환)해야한다.   

```
int(input())    # str -> int 캐스팅
```

### - 출력
```
print({출력내용1}, {출력내용2}, ... , sep = ' ', end = '\n' )    
```

sep : 출력내용이 여러개가 있다면 sep의 값이 중간에 삽입 (기본값 ' ')   
end : 출력내용을 모두 출력한 후 마지막에 출력할 문자열 (기본값 '\n')   
.   
.   
.   
- - -
## 3. 파일 읽고 쓰기
### 파일 열기
``` 
file = open({파일경로}, mode = 'r')    # 반환값을 변수로 받아서 사용함
```
파일의 경로와 모드에 대한 설명은 아래에 있습니다.

### 파일 닫기
```
file.close()
```
메모리 누수 방지를 위해 파일을 닫아주어야 한다.   
   
### 파일 쓰기
```
file.write({입력내용})
```
입력내용을 해당 파일에 출력한다.   
.    
.   
### - 파일의 경로
- 절대경로   
``` "C:/users/user/..." ``` 와 같이 가장 상위 디렉토리부터 경유하는 경로를 모두 기입한다.   
   
- 상대경로   
현재 디렉토리를 기준으로 경로를 기입한다.   
``` / ```       : 현재 디렉토리의 최상위 디렉토리
``` ./ ```      : 현재 디렉토리
``` ../ ```     : 현재 디렉토리의 상위 디렉토리   
   
### - 파일 열기 모드
|모드|설명        
|----|------------
|r   |읽기모드   
|w   |쓰기모드   
|x   |파일이 없으면 파일 생성하고 쓰기모드로 열림 (파일 있으면 에러)   
|a   |추가모드 (파일의 마지막에 내용 추가)   

.   
.   
.   