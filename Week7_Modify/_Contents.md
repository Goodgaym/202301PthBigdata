# 목차
> 1. 데이터 프레임
> 2. 데이터 삭제하기
> 3. 데이터 수정하기

- - -
.loc[]
: 데이터 프레임에서 행/열을 선택하는 메서드
```
{데이터프레임}.loc[{행 인덱싱}, {열 인덱싱}]
```

프레임 데이터의 columns는 index로 저장되어 있음

.drop()
: 데이터 프레임에서 행/열을 선택하여 삭제
```
{데이터 프레임}.drop({삭제하고자 하는 위치}, axis, inplace)
```
axis = 0:행삭제, 1:열삭제
inplace = True:현재 데이터프레임에 덮어씌우기, False:현재 데이터프레임 유지하고 결과 반환

.dropna()
: NaN이 하나 이상 포함된 행이나 열 삭제
```

```

how = 'all':모든 값이 NaN인 열 삭제